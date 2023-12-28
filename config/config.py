import configparser
import json
import os


def get_config():
    # 创建一个配置解析器对象
    config = configparser.ConfigParser()
    config.read('.env')

    # 配置 openai 环境变量
    os.environ['OPENAI_BASE_URL'] = config.get('openai', 'base_url')
    os.environ['OPENAI_API_KEY'] = config.get('openai', 'api_key')

    # 设置代理
    http_proxy = config.get('openai', 'http_proxy')
    https_proxy = config.get('openai', 'https_proxy')
    if http_proxy:
        os.environ['http_proxy'] = http_proxy
    if https_proxy:
        os.environ['https_proxy'] = https_proxy

    return config


def get_prob_data():
    current_dir = os.path.dirname(__file__)

    with open(f'{current_dir}/leetcode_probs.txt', 'r') as f:
        prob_dict = json.loads(f.read())

    return prob_dict


def get_algo_gr():
    current_dir = os.path.dirname(__file__)

    with open(f'{current_dir}/geekxh_algo_gr.txt', 'r') as f:
        xh_gr_dict = json.loads(f.read())

    return xh_gr_dict


prob_dict = get_prob_data()

algo_gr_dict = get_algo_gr()

lang_list = ['C++', 'Java', 'Python', 'Python3', 'C', 'C#', 'JavaScript', 'TypeScript', 'PHP', 'Swift', 'Kotlin',
             'Dart', 'Go', 'Ruby', 'Scala', 'Rust', 'Racket', 'Erlang', 'Elixir']
