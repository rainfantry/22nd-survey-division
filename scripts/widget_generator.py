#!/usr/bin/env python3
"""
22nd Survey Division — Widget Generator
Builds interactive HTML widgets from real lab data.

Usage:
    python widget_generator.py --module 12 --title "ETW Bypass" --tabs theory,recon,exploit,demo,detection,lab
"""

import argparse
import json
import os
import re
from datetime import datetime

# Template paths
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
WIDGET_DIR = os.path.join(os.path.dirname(__file__), "..", "widgets")
LAB_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "lab_data")


def load_template():
    """Load the base widget HTML template."""
    template_path = os.path.join(TEMPLATE_DIR, "widget-template.html")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()


def load_lab_data(module_id):
    """Load real lab data for a module."""
    data_path = os.path.join(LAB_DATA_DIR, f"module_{module_id:02d}_data.json")
    if os.path.exists(data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def generate_tabs(tab_names):
    """Generate tab buttons HTML."""
    tabs_html = []
    for i, name in enumerate(tab_names):
        active = "active" if i == 0 else ""
        tabs_html.append(f'    <button class="tab {active}" onclick="showTab(\'tab{i+1}\')">{name.upper()}</button>')
    return "\n".join(tabs_html)


def generate_tab_content(tab_names, lab_data):
    """Generate tab content divs with real lab data."""
    content_html = []
    
    # Default content for each tab type
    default_content = {
        "theory": "<p>Theory content placeholder. Replace with real explanation.</p>",
        "recon": "<p>Reconnaissance commands and output.</p>",
        "exploit": "<p>Exploit technique and code.</p>",
        "demo": "<p>Live demonstration with real output.</p>",
        "detection": "<p>Detection vectors and blue team perspective.</p>",
        "lab": "<p>Hands-on lab exercise.</p>"
    }
    
    for i, name in enumerate(tab_names):
        active = "active" if i == 0 else ""
        
        # Get real data for this tab if available
        tab_data = lab_data.get(name.lower(), {})
        commands = tab_data.get("commands", [])
        
        content_blocks = []
        for cmd in commands:
            command_text = cmd.get("command", "")
            output_text = cmd.get("output", "")
            note_text = cmd.get("note", "")
            
            block = f'''<div class="cmd-block">
      <button class="copy-btn" onclick="copyCommand(this)">COPY</button>
      <span class="prompt">$</span> <span class="command">{command_text}</span>
      <div class="output">{output_text}</div>
    </div>'''
            if note_text:
                block += f'\n    <div class="note">{note_text}</div>'
            
            content_blocks.append(block)
        
        # If no real data, use placeholder
        if not content_blocks:
            content_blocks.append(default_content.get(name.lower(), f"<p>{name} content.</p>"))
        
        content_html.append(f'''<div id="tab{i+1}" class="content {active}">
    {chr(10).join(content_blocks)}
  </div>''')
    
    return "\n\n".join(content_html)


def generate_widget(module_id, title, first_principle, tab_names, lab_data):
    """Generate complete widget HTML."""
    template = load_template()
    
    # Replace placeholders
    widget_html = template.replace("{{MODULE_TITLE}}", title)
    widget_html = widget_html.replace("{{MODULE_ID}}", f"{module_id:02d}")
    widget_html = widget_html.replace("{{FIRST_PRINCIPLE}}", first_principle)
    widget_html = widget_html.replace("{{TABS}}", generate_tabs(tab_names))
    widget_html = widget_html.replace("{{TAB_CONTENT}}", generate_tab_content(tab_names, lab_data))
    
    return widget_html


def save_widget(module_id, html_content):
    """Save widget to file."""
    os.makedirs(WIDGET_DIR, exist_ok=True)
    filename = f"module_{module_id:02d}_widget.html"
    filepath = os.path.join(WIDGET_DIR, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[+] Widget saved: {filepath}")
    return filepath


def main():
    parser = argparse.ArgumentParser(description="22nd Survey Division Widget Generator")
    parser.add_argument("--module", type=int, required=True, help="Module ID (e.g., 12)")
    parser.add_argument("--title", type=str, required=True, help="Module title")
    parser.add_argument("--principle", type=str, default="Understanding internals beats copy-paste.", help="First principle")
    parser.add_argument("--tabs", type=str, default="theory,recon,exploit,demo,detection,lab", help="Comma-separated tab names")
    parser.add_argument("--data", type=str, help="Path to lab data JSON file")
    
    args = parser.parse_args()
    
    tab_names = [t.strip() for t in args.tabs.split(",")]
    
    # Load lab data
    lab_data = {}
    if args.data:
        with open(args.data, "r", encoding="utf-8") as f:
            lab_data = json.load(f)
    else:
        lab_data = load_lab_data(args.module)
    
    # Generate widget
    html = generate_widget(args.module, args.title, args.principle, tab_names, lab_data)
    
    # Save
    filepath = save_widget(args.module, html)
    
    print(f"[+] Generated Module {args.module:02d}: {args.title}")
    print(f"[+] Tabs: {', '.join(tab_names)}")
    print(f"[+] Output: {filepath}")


if __name__ == "__main__":
    main()
