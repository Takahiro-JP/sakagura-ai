import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from claude_client import generate_post
from database import search_products, save_post

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot起動: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command()
async def post(ctx, product: str, *, target: str):
    products = search_products(product)
    if not products:
        await ctx.send(f"「{product}」は見つかりませんでした")
        return

    p = products[0]
    await ctx.send(f"「{p['name']}」で生成中...")

    result = generate_post(p, target)

    if "error" in result:
        await ctx.send(result["error"])
        return

    # 各プラットフォームをDBに保存
    for platform, content in result.items():
        save_post(p["id"], platform, content, target)

    # Discordに表示
    output = f"""
**【Instagram】**
{result['instagram']}

**【X（Twitter）】**
{result['x']}

**【Facebook】**
{result['facebook']}
"""
    await ctx.send(output)

bot.run(os.getenv("DISCORD_TOKEN"))