import re

import requests
from bs4 import BeautifulSoup


def trans_md(content):
    in_eg = False  # 是否进入示例区
    md_content = []

    for i, part_content in enumerate(content.split('\n')):
        if i == 0:
            match = re.search(r"(\d+)\.\s+(.*?)\s+-\s+(.*)", part_content)
            if match:
                part_content = match.group(3)
        elif re.match(r'\[http(.*?)\]', part_content):
            part_content = re.sub(r'\[(.*?)\]', r'![image](\1)', part_content)
        elif re.match(r'^示例\s\d+[：:]$', part_content) or re.match(r'^示例[：:]$', part_content):
            in_eg = True
            part_content = f'**{part_content}**'
        elif re.match(r'^提示：$', part_content):
            part_content = f'**{part_content}**'
        elif in_eg:
            if part_content == '\xa0':
                in_eg = False
            else:
                if re.match(r'输入：|输出：|解释：', part_content):
                    exp_sub_title = re.findall(r'输入：|输出：|解释：', part_content)[0]
                    part_content = part_content.replace(exp_sub_title, f'>\n>**{exp_sub_title}** ')
                elif part_content != '':
                    part_content = f'>\n>{part_content}'

        md_content.append(part_content)

    return '\n'.join(md_content)


def get_leetcode_prob(prob_url):
    req_res = requests.get(prob_url)

    try:
        prob_bs = BeautifulSoup(req_res.text, 'html.parser')
        prob_meta = prob_bs.find('meta', {'name': 'description'})

        content = prob_meta.get('content', None)
        return trans_md(content)
    except:
        pass

    return None


