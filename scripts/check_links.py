#!/usr/bin/env python3
"""
22nd Survey Division — Link Checker
Scans all HTML files for broken internal links.
Usage: python check_links.py <repo_dir>
"""

import os
import sys
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

def find_html_files(repo_dir):
    """Find all HTML files in the repo."""
    html_files = []
    for root, _, files in os.walk(repo_dir):
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    return html_files

def extract_links(html_path, repo_dir):
    """Extract all href/src links from an HTML file, excluding code blocks."""
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove code blocks to avoid false positives on code snippets
    content = re.sub(r'<pre.*?</pre>', '', content, flags=re.DOTALL)
    content = re.sub(r'<code.*?</code>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="code-block".*?</div>', '', content, flags=re.DOTALL)
    
    # Find href and src attributes
    links = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    
    # Filter to internal links only (not http://, https://, mailto:, etc.)
    internal = []
    for link in links:
        if link.startswith(('http://', 'https://', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        internal.append(link)
    
    return internal

def check_link(link, source_file, repo_dir):
    """Check if a link resolves to an existing file."""
    source_dir = os.path.dirname(source_file)
    
    # Skip data URIs
    if link.startswith('data:'):
        return True, "data URI"
    
    # Skip anchor-only links
    if link.startswith('#'):
        return True, "anchor"
    
    # Resolve relative to source file
    if link.startswith('/'):
        # Absolute from repo root
        target = os.path.join(repo_dir, link.lstrip('/'))
    else:
        # Relative to source file
        target = os.path.normpath(os.path.join(source_dir, link))
    
    # Check if target exists (as file or with .html)
    if os.path.exists(target):
        return True, target
    if os.path.exists(target + '.html'):
        return True, target + '.html'
    
    # Special case: modules linking to index.html should be ../index.html
    if 'modules' in source_dir and link == 'index.html':
        parent_target = os.path.normpath(os.path.join(source_dir, '..', link))
        if os.path.exists(parent_target):
            return True, parent_target
    
    # Special case: anchor links like index.html#section
    if '#' in link:
        base = link.split('#')[0]
        if base == '' or base == os.path.basename(source_file):
            return True, "same-page anchor"
        base_target = os.path.normpath(os.path.join(source_dir, base))
        if os.path.exists(base_target) or os.path.exists(base_target + '.html'):
            return True, base_target
    
    return False, target

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_links.py <repo_dir>")
        sys.exit(1)
    
    repo_dir = sys.argv[1]
    html_files = find_html_files(repo_dir)
    
    broken = []
    total = 0
    
    for html_file in html_files:
        links = extract_links(html_file, repo_dir)
        for link in links:
            total += 1
            ok, target = check_link(link, html_file, repo_dir)
            if not ok:
                rel_source = os.path.relpath(html_file, repo_dir)
                broken.append((rel_source, link, os.path.relpath(target, repo_dir)))
    
    if broken:
        print(f"  ✗ {len(broken)}/{total} links broken:")
        for source, link, target in broken:
            print(f"    {source} -> {link} (expected: {target})")
        sys.exit(1)
    else:
        print(f"  ✓ All {total} internal links valid")
        sys.exit(0)

if __name__ == '__main__':
    main()
