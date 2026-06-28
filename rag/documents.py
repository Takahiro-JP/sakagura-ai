import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rag.retriever import add_document

def load_documents():
    # 蔵元の歴史
    add_document(
        doc_id="history_1",
        text="""
        楯野川酒造は山形県酒田市に蔵を構える日本酒蔵元です。
        創業は文化元年（1804年）で、200年以上の歴史を持ちます。
        「純米大吟醸専門蔵」として、全量純米大吟醸を製造しています。
        世界30カ国以上に輸出しており、海外でも高い評価を得ています。
        """,
        metadata={"type": "history"}
    )

    # 商品情報：清流
    add_document(
        doc_id="product_seiryu",
        text="""
        楯野川 純米大吟醸 清流はBasicシリーズの定番商品です。
        精米歩合50%で丁寧に磨いたお米を使用しています。
        穏やかな香りと柔らかな口当たりが特徴で、食中酒として最適です。
        価格は1,650円（税込）でお求めやすい価格帯です。
        山形県産の酒米を使用し、清らかな水で醸しています。
        日本酒初心者から愛好家まで幅広く楽しめる一本です。
        """,
        metadata={"type": "product", "name": "清流"}
    )

    # 商品情報：極限
    add_document(
        doc_id="product_kyokugen",
        text="""
        楯野川 純米大吟醸 極限はExtremeシリーズの最高峰です。
        精米歩合35%まで磨き上げた究極の純米大吟醸です。
        華やかな吟醸香と繊細な甘みが特徴です。
        価格は3,300円（税込）です。
        特別な日のプレゼントや記念日にふさわしい一本です。
        """,
        metadata={"type": "product", "name": "極限"}
    )

    # 商品情報：SAKERISE
    add_document(
        doc_id="product_sakerise",
        text="""
        SAKERISEは楯野川の新ブランドで、日本酒の新しい楽しみ方を提案します。
        20代・30代の若い世代をターゲットにした商品です。
        精米歩合35%の純米大吟醸でありながら、革新的なパッケージデザインが特徴です。
        「暁光」は価格8,800円（税込）のプレミアム商品です。
        日本酒文化を世界に広める楯野川の挑戦的なブランドです。
        """,
        metadata={"type": "product", "name": "SAKERISE"}
    )

    # 醸造へのこだわり
    add_document(
        doc_id="brewing_1",
        text="""
        楯野川酒造の醸造へのこだわりは「全量純米大吟醸」にあります。
        アルコール添加を一切行わず、米と水と麹だけで醸します。
        仕込み水には鳥海山の伏流水を使用しています。
        酒米は山形県産の雪女神・出羽燦々などを使用しています。
        低温でゆっくりと発酵させることで、繊細な香りと味わいを引き出します。
        """,
        metadata={"type": "brewing"}
    )

    print("ドキュメント登録完了")

if __name__ == "__main__":
    load_documents()