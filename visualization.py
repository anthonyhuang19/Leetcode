import os
import re
from datetime import datetime
import urllib.parse
import json

def parse_problem_info(filename):
    """Extract problem number, name, and difficulty from filename"""
    match = re.match(r'(\d+)\s+(.*?)_(Easy|Medium|Hard)\.md', filename)
    if match:
        return {
            'number': int(match.group(1)),
            'name': match.group(2),
            'difficulty': match.group(3)
        }
    return None

def count_solved_problems():
    stats = {
        'total': 0,
        'by_platform': {},
        'by_difficulty': {'Easy': 0, 'Medium': 0, 'Hard': 0},
        'problems': [],
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Loop through all files in the current directory
    for file in os.listdir('.'):
        if file.endswith('.md'):
            problem_info = parse_problem_info(file)
            if problem_info:
                problem_info['platform'] = 'Local'
                
                # Replace spaces with %20 and generate GitHub URL for each problem
                github_url = f"https://github.com/anthonyhuang19/Leetcode/blob/master/{urllib.parse.quote(file)}"
                problem_info['path'] = github_url
                stats['problems'].append(problem_info)
                stats['by_difficulty'][problem_info['difficulty']] += 1
                stats['total'] += 1
    
    stats['problems'].sort(key=lambda x: x['number'])
    return stats

def generate_readme(stats):
    total = stats['total']
    easy_pct = (stats['by_difficulty']['Easy'] / total) * 100 if total > 0 else 0
    medium_pct = (stats['by_difficulty']['Medium'] / total) * 100 if total > 0 else 0
    hard_pct = (stats['by_difficulty']['Hard'] / total) * 100 if total > 0 else 0
    
    # Create chart config dictionary for URL
    chart_config = {
        'type': 'doughnut',
        'data': {
            'labels': ['Easy', 'Medium', 'Hard'],
            'datasets': [{
                'data': [
                    stats['by_difficulty']['Easy'],
                    stats['by_difficulty']['Medium'],
                    stats['by_difficulty']['Hard']
                ],
                'backgroundColor': ['#4CAF50', '#FFC107', '#F44336']
            }]
        }
    }
    
    # Convert dictionary to JSON and then URL-encode it
    chart_url = f"https://quickchart.io/chart?c={urllib.parse.quote(json.dumps(chart_config))}&width=300&height=300"
    
    # Template for the README
    template = """# 📚 Algorithmic Problem Solutions

*"Pursuing elegant solutions to computational problems"*  
*Last Updated: {last_updated}*

## 📊 Statistics Overview

| Metric            | Count |
|-------------------|-------|
| Total Problems    | {total} |
| Easy              | {easy_count} ({easy_pct:.1f}%) |
| Medium            | {medium_count} ({medium_pct:.1f}%) |
| Hard              | {hard_count} ({hard_pct:.1f}%) |

### 🏆 Platform Distribution
{platform_distribution}

## 🧩 Solved Problems Table

| #  | Problem Name | Difficulty | Solution |
|----|--------------|------------|----------|
"""
    # Format the template with dynamic data
    formatted_template = template.format(
        last_updated=stats['last_updated'],
        total=stats['total'],
        easy_count=stats['by_difficulty']['Easy'],
        easy_pct=easy_pct,
        medium_count=stats['by_difficulty']['Medium'],
        medium_pct=medium_pct,
        hard_count=stats['by_difficulty']['Hard'],
        hard_pct=hard_pct,
        platform_distribution='Local: {total}'.format(total=stats['total'])
    )
    
    # Add solved problems to the table
    for problem in stats['problems'][-10:]:
        difficulty_emoji = {
            'Easy': '🟢',
            'Medium': '🟡',
            'Hard': '🔴'
        }.get(problem['difficulty'], '')
        
        formatted_template += f"| {problem['number']} | {problem['name']} | {difficulty_emoji} {problem['difficulty']} | [View]({problem['path']}) |\n"
    
    # Add chart visualization
    formatted_template += f"""
## 📈 Progress Visualization

![Difficulty Distribution]({chart_url})

*"The art of programming is the art of organizing complexity."*  
*— Edsger W. Dijkstra*
"""
    
    # Write the generated template to README.md
    with open('README.md', 'w') as f:
        f.write(formatted_template)

if __name__ == '__main__':
    stats = count_solved_problems()
    generate_readme(stats)
