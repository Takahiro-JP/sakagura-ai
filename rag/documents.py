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

    # rag/documents.py に追記
    add_document(
        doc_id="press_sake360",
        text="""
        楯の川酒造は2026年、酒蔵からライフスタイル企業へ転換する「SAKE 360° Lifestyle」を発表。
        お酒を「飲むもの」から「人生を楽しむ体験」へ進化させる。
        世界主要都市に体験型BAR「THE BAR」を展開予定。第一弾は東京。
        20歳の「最初の一杯」をデザインするFIRST LOVEプロジェクト始動。
        山形の食・工芸との共創による価値創出「YAMAGATA SYNERGY」を推進。
        世界中の人が酒造りに参加できるグローバルコミュニティを構築予定。
        代表取締役：佐藤淳平（六代目蔵元）、創業：天保三年（1832年）。
        """,
        metadata={"type": "press_release", "date": "2026-04-01"}
    )
    
    # シルスマリアコラボ
    add_document(
        doc_id="press_chocolate",
        text="""
        楯の川酒造とシルスマリアのコラボ商品「楯野川 主流 生チョコレート」が期間限定発売。
        使用日本酒は楯野川 純米大吟醸「主流」。兵庫県産山田錦を使用し、華やかな香りと上品な余韻が特徴。
        価格3,132円（税込）、16粒入り、アルコール分1.6%。
        昨年は全国で約2万個を販売しバレンタイン前に完売した人気商品。
        ペアリングセットも展開：主流セット6,050円、無我レッドボトルセット6,270円、ヨー子セット6,270円。
        楯の川酒造は精米歩合1%という極限まで磨いた高精白日本酒にも挑戦している。
        """,
        metadata={"type": "press_release", "date": "2026-02-02"}
    )
    
    print("ドキュメント登録完了")

if __name__ == "__main__":
    load_documents()