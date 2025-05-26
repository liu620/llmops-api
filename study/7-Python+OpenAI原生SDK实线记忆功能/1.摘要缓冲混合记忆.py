from typing import Any

import dotenv
from openai import OpenAI

dotenv.load_dotenv()


# 1. max_tokens 最大摘要长度
# 2. summary用于存储摘要信息
# 3. chat_history用于纯出历史对话
# 4. get_num_token 用于技术传入文本呢的token
# 5. save_context用于存储新的交流对话
# 6. get_buffer_string 用于将历史对话转化为字符串
# 7. summer_text 用于将旧的摘要和传入的对话生成新摘要
class ConversationSummaryBufferMemory:
    '''摘要缓存混合记忆'''

    def __init__(self, summary: str = '', chat_histories: list = None, max_tokens: int = 300):
        self.summary = summary
        self.chat_histories = [] if chat_histories is None else chat_histories
        self.max_tokens = max_tokens
        self._client = OpenAI(base_url="https://api.deepseek.com/v1")
        pass

    @classmethod
    def get_num_tokens(cls, query: str) -> int:
        """获取计算传入的query的token数"""
        return len(query)

    def save_context(self, human_query: str, ai_content: str) -> None:
        """保存传入的新一次对话信息"""
        self.chat_histories.append({"human": human_query, "ai": ai_content})

        buff_string = self.get_buff_string()
        tokens = self.get_num_tokens(buff_string)
        if tokens > self.max_tokens:
            first = self.chat_histories[0]
            print("摘要生成中~")
            self.summary = self.summary_text(
                self.summary,
                f"Human:{first.get('human')} \nAI:{first.get('ai')}")
            print("新的摘要生成成功: ", self.summary)
            del self.chat_histories[0]

    def get_buff_string(self) -> str:
        """将历史对话转化成字符串"""
        buff: str = ""
        for chat in self.chat_histories:
            buff += f"Human:{chat.get('human')} \nAI:{chat.get('ai')} \n\n"

        return buff.strip()

    def load_memory_variables(self) -> dict[str, Any]:
        """加载记忆变量为一个字典，便于格式化到prompt中"""
        buff_string = self.get_buff_string()
        return {
            "chat_histories": f"摘要：{self.summary} \n 历史信息：{buff_string} \\n"
        }

    def summary_text(self, origin_summary: str, new_line: str) -> str:
        prompt = f"""
        ====
        你是一个强大的聊天机器人，请根据用户提供的谈话内容，总结摘要，并将其添加到先前提供的摘要中，反回一个新的摘要，除了摘要其他人和数据都不要生成，如果用户的对话信息里有一些关键信息，比如说姓名、爱好、性别、重要事件等，这些全部都要包括在摘要中，摘要尽可能要还原用户的对话记录，
        请不要将<example>标签里的数据当城实际的数据，这里的数据只是一个示例，告诉你如何生成摘要。
        
        <example>
        当前摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量。
        新的对话：
        Human: 为什么你认为人工智能是一股向善的力量?
        AI: 因为人工智能会充分发挥潜力
        
        新摘要：人类会问人工智能对人工智能的看法，人工智能认为人工智能是一股向善的力量，因为它将帮助人类充分发挥潜力。
        </example>
        ========================以下的数据是实际需要处理的数据==========================
        当前摘要:{origin_summary}
        新的对话：
        {new_line}
        """

        completion = self._client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content


client = OpenAI(base_url="https://api.deepseek.com/v1")

memory: ConversationSummaryBufferMemory = ConversationSummaryBufferMemory("", [], 300)

while True:
    query = input('Human:')

    if query == 'q':
        break

    memory_variable = memory.load_memory_variables()
    answer_prompt = (
        "你是一个强大的聊天机器人，请根据上下文和用户提问解决问题。\n\n"
        f"{memory_variable.get('chat_histories')} \n\n"
        f"用户的提问是：{query}"
    )
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[
            {'role': 'user', 'content': answer_prompt}
        ],
        stream=True
    )
    print("AI:", flush=True, end='')
    ai_content = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content is None:
            break

        ai_content += content
        print(content, flush=True, end='')
    print('')
    memory.save_context(query, ai_content)
