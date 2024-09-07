import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import io

    # 디스코드 봇 토큰
    TOKEN = 'MTI3MTc0MjgyODEwNzY2NTQ2Mg.GTbkr7.4lcPfkh_v8qnl1oOVLF3sFytGcktQl4Kpyhzj0'

    # 디스코드 Intents 설정
    intents = discord.Intents.default()
    intents.message_content = True  # 메시지 내용을 읽을 수 있도록 인텐트 활성화

    # 디스코드 봇 설정
    bot = commands.Bot(command_prefix="/", intents=intents)

    # !capture 명령어가 입력될 때 실행
    @bot.command()
    async def 랭크(ctx):
        # 크롬 드라이버 옵션 설정
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # GUI 없이 실행
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # 크롬 드라이버 설정 (webdriver-manager로 자동 관리)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
        try:
            # 웹 페이지 접속
            driver.get("https://ch.tetr.io/league/")
        
            # 'RANK BREAKDOWN' 요소 찾기
            element = driver.find_element(By.ID, "tlchart_wrapper")  # 해당 요소의 클래스 이름을 사용

            # 요소 스크린샷 캡처
            screenshot = element.screenshot_as_png

            # 스크린샷 이미지를 디스코드로 전송
            await ctx.send(file=discord.File(io.BytesIO(screenshot), 'rank_breakdown.png'))

        finally:
            # 드라이버 종료
            driver.quit()

    # 봇 실행
    bot.run(TOKEN)
