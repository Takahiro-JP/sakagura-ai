import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import init_db, add_product

init_db()

add_product("楯野川 純米大吟醸 清流", "Basic", 50, 1650, "穏やかな香りと柔らかな口当たり。食中酒として最適。", "全世代")
add_product("楯野川 純米大吟醸 極限", "Extreme", 35, 3300, "華やかな吟醸香と繊細な甘み。特別な日に。", "30-40代")
add_product("楯野川 無我 プラチナ", "無我", 40, 5500, "上品な甘みと余韻。贈り物に最適。", "30-40代")
add_product("SAKERISE 暁光", "SAKERISE", 35, 8800, "新感覚の日本酒体験。若い世代への入り口。", "20代")

print("初期データ投入完了")