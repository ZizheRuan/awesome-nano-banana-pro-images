#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to reverse the order of cases in README.md
Changes the order from Case 1-32 to Case 32-1
"""

import re
from pathlib import Path


def reverse_cases_in_readme():
    """Reverse the order of cases in README.md"""
    
    readme_path = Path(__file__).parent.parent / "README.md"
    
    # Read the file
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Split the content into sections
    # 1. Everything before the cases list
    # 2. The cases list (TOC)
    # 3. Everything between TOC and actual cases
    # 4. The actual cases section
    # 5. Everything after cases (Acknowledge section)
    
    # Find the cases list section
    toc_start = content.find("- [✨ Cases list](#️-cases)")
    toc_end = content.find("\n## ✨ Cases\n")
    
    # Find the actual cases section
    cases_start = toc_end
    cases_end = content.find("\n## 🙏 Acknowledge\n")
    
    # Extract sections
    before_toc = content[:toc_start]
    toc_section = content[toc_start:toc_end]
    cases_section = content[cases_start:cases_end]
    after_cases = content[cases_end:]
    
    # Extract individual TOC entries (skip the first line which is "- [✨ Cases list]...")
    toc_lines = toc_section.split("\n")
    header_line = toc_lines[0]  # "- [✨ Cases list](#️-cases)"
    case_links = [line for line in toc_lines[1:] if line.strip().startswith("- [Case")]
    
    # Reverse the TOC entries
    case_links.reverse()
    
    # Rebuild TOC section
    new_toc = header_line + "\n" + "\n".join(case_links)
    
    # Extract individual case sections
    # Split by "### Case" but keep the delimiter
    case_pattern = r'(### Case \d+:.*?)(?=### Case \d+:|$)'
    cases = re.findall(case_pattern, cases_section, re.DOTALL)
    
    # Reverse the cases
    cases.reverse()
    
    # Rebuild cases section with the header
    new_cases_section = "\n## ✨ Cases\n" + "".join(cases)
    
    # Combine all sections
    new_content = before_toc + new_toc + new_cases_section + after_cases
    
    # Write back to file
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"✅ Successfully reversed the order of cases in {readme_path}")
    print(f"   Cases are now ordered from Case 32 to Case 1")


if __name__ == "__main__":
    reverse_cases_in_readme()
