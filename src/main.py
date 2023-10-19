from crawler import Crawler
from slack import post_slack

if __name__ == "__main__":
    url = 'https://localhost:5555/'
    TARGET_CLASS_NAME = 'slack'

    crawler = Crawler(url, TARGET_CLASS_NAME)
    # screenshotを取得
    image = crawler.crawl()

    # slack post
    post_slack(image.getvalue())
    
