import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import arxiv
import openai
import random
import requests

from paperpal.config import Config

SLACK_CHANNEL = "#fun-daily-thesis"
SLACK_API_KEY=os.environ.get('SLACK_API_KEY')
QUERY_API_ENDPOINT=os.environ.get('QUERY_API_ENDPOINT')

def get_summary(result):

    gpt_query_txt = """上の論文の要点を3点のみでまとめ、以下のフォーマットで日本語で出力してください。```
    タイトルの日本語訳
    ・要点1
    ・要点2
    ・要点3
    ```"""
    text = f"以下はとある論文のタイトルとアブストラクトです。\ntitle: {result.title}\nbody: {result.summary}"

    gpt_query_txt = text + '\n' + gpt_query_txt
    gpt_query_json = {
        'username' : "bot-daily-thesis",
        'content' : gpt_query_txt
    }
    summary = requests.post(QUERY_API_ENDPOINT, json=gpt_query_json, timeout=20)
    summary = summary.text.json()['response']
    # summary = response['choices'][0]['message']['content']
    title_en = result.title
    title, *body = summary.split('\n')
    body = '\n'.join(body)
    date_str = result.published.strftime("%Y-%m-%d %H:%M:%S")
    message = f"発行日: {date_str}\n{result.entry_id}\n{title_en}\n{title}\n{body}\n"
    
    return message

def main(event, context):
    # Slack APIクライアントを初期化する
    client = WebClient(token=SLACK_API_KEY)
    config : Config = Config()
    
    keywords = [topic.topic_name for topic in config.registered_topics]

    for j, keyword in enumerate(keywords):
        #queryを用意、今回は、三種類のqueryを用意
        query =f'ti:%22 {keyword} %22'

        # arxiv APIで最新の論文情報を取得する
        search = arxiv.Search(
            query=query,  # 検索クエリ（
            max_results=100,  # 取得する論文数
            sort_by=arxiv.SortCriterion.SubmittedDate,  # 論文を投稿された日付でソートする
            sort_order=arxiv.SortOrder.Descending,  # 新しい論文から順に取得する
        )
        #searchの結果をリストに格納
        result_list = []
        for result in search.results():
            result_list.append(result)
        #ランダムにnum_papersの数だけ選ぶ
        num_papers = 1
        results = random.sample(result_list, k=num_papers)
        
        # 論文情報をSlackに投稿する
        for i, result in enumerate(results):
            try:
                # Slackに投稿するメッセージを組み立てる
                message = "今日の論文です！ " + str(j * num_papers + i + 1) + "本目 " + f"keyword : {keyword}\n" + get_summary(result)
                # Slackにメッセージを投稿する
                response = client.chat_postMessage(
                    channel=SLACK_CHANNEL,
                    text=message
                )
                print(f"Message posted: {response['ts']}")
            except SlackApiError as e:
                print(f"Error posting message: {e}")

if __name__ == "__main__":
    main(None, None)