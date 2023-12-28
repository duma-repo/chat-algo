import gradio as gr
import gr_funcs

from config import config

css = """
    #box_shad { box-shadow: 0px 0px 1px rgba(0, 0, 0, 0.6); /* 设置阴影 */ }
    .problem-class {
        height: 555px;
        overflow-y: scroll;
        background-color: #ffffff;
        padding-left: 15px;
    }
    """


def main():
    with gr.Blocks(title="chat-algo AI陪你玩算法", theme=gr.themes.Soft(), css=css) as demo:
        prob_selector = gr.Dropdown(label='选择力扣算法题目', choices=config.prob_dict)

        with gr.Row():
            with gr.Column(scale=2):
                prob_info_md = gr.Markdown()
                prob_content_md = gr.Markdown('请选择一道题目', elem_classes='problem-class')
                with gr.Row():

                    code_lang_selector = gr.Dropdown(container=False, value='Python', choices=config.lang_list,
                                                     interactive=True)
                    solve_prob_btn = gr.Button('解析此题目', variant='primary')
            with gr.Column(scale=3):
                algo_chatbot = gr.Chatbot(label='AI算法助手', height=600)
                with gr.Row():
                    chat_input = gr.Text(container=False, scale=6)
                    chat_send_btn = gr.Button('发送', variant='primary')
                    chat_clear_btn = gr.Button('清空', variant='stop')

        with gr.Accordion('算法知识点', open=False):
            with gr.Tab('算法图解'):
                algo_gr_html = gr.HTML()


        # 事件监听
        # 选择题目
        prob_selector.change(gr_funcs.select_prob, inputs=[prob_selector], outputs=[prob_content_md, prob_info_md])

        # 解析题目
        solve_prob_btn.click(gr_funcs.solve_algo_prob,
                             inputs=[prob_content_md, code_lang_selector, algo_chatbot],
                             outputs=[algo_chatbot])

        # chat按钮
        chat_send_btn.click(gr_funcs.chat_send, inputs=[chat_input, algo_chatbot], outputs=[algo_chatbot])
        chat_send_btn.click(lambda: '', outputs=[chat_input])
        chat_clear_btn.click(lambda: [], outputs=[algo_chatbot])

        # 知识点交互
        prob_selector.change(gr_funcs.render_algo_gr, inputs=[prob_selector], outputs=[algo_gr_html])

    demo.launch()


if __name__ == '__main__':
    main()