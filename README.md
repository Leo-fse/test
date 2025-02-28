import pandas as pd
import numpy as np
import ipywidgets as widgets
from datetime import datetime, timedelta
from IPython.display import display, clear_output, HTML

# 表示用のOutputウィジェット
out = widgets.Output()

# ダミーデータ作成関数
def create_dummy_data():
    duplicate_num = 4  # 0 にするとデータなしの状態をシミュレート
    start = datetime(2024, 1, 10)
    
    df_list = []
    for idx in range(duplicate_num):
        time_shift = timedelta(days=idx)
        start_date = start + time_shift
        end_date = start_date + timedelta(days=3)
        
        d_range = pd.date_range(start=start_date, end=end_date, freq="D")
        
        # ダミーデータ作成
        data_values = np.random.randint(1, 100, size=(len(d_range), 2))
        
        df_1 = pd.DataFrame(data_values[:, 0], index=d_range, columns=["columnA"])
        df_2 = pd.DataFrame(data_values[:, 1], index=d_range, columns=["columnB"])
        
        df_list.append((df_1, df_2))
    
    return df_list

# 2つのデータフレームを横並びで表示する
def show_dataframes_side_by_side(df1, df2):
    html_content = f"""
    <div style='display: flex; justify-content: center; gap: 20px;'>
        <div style="max-width: 45%; border: 1px solid #ccc; padding: 10px;">
            <h3>DataFrame 1</h3>
            {df1.head(5).to_html()}
        </div>
        <div style="max-width: 45%; border: 1px solid #ccc; padding: 10px;">
            <h3>DataFrame 2</h3>
            {df2.head(5).to_html()}
        </div>
    </div>
    """
    display(HTML(html_content))

# ダミーデータ作成
dummy_data_list = create_dummy_data()

# 処理中のインデックス
current_index = 0

# ドロップダウン作成
dropdown = widgets.Dropdown(
    options=["Yes", "No"],
    value="No",
    description="上書き:",
    layout=widgets.Layout(width="150px")
)

# 次へボタン
next_button = widgets.Button(description="次へ", layout=widgets.Layout(width="80px"))

# 次のデータを表示する関数
def process_next_data(button):
    global current_index

    with out:
        out.clear_output(wait=True)  # 出力をクリア
        
        if current_index < len(dummy_data_list):
            df1, df2 = dummy_data_list[current_index]
            print(f"データ {current_index + 1}/{len(dummy_data_list)} の処理中")
            
            # "Yes" を選択した場合はデータを更新（ここでは単にメッセージを表示）
            if dropdown.value == "Yes":
                print("データを上書きしました。")
            else:
                print("データを上書きしませんでした。")

            show_dataframes_side_by_side(df1, df2)
            current_index += 1  # 次のデータへ

        if current_index >= len(dummy_data_list):
            print("すべてのデータの処理が完了しました。")
            next_button.disabled = True  # 最後のデータならボタンを無効化

# ボタンのクリックイベントに関数を登録
next_button.on_click(process_next_data)

# データがある場合のみウィジェットを表示
if dummy_data_list:
    display(dropdown, next_button, out)
    process_next_data(None)  # 最初のデータを表示
else:
    display(HTML("<p style='color: red; font-weight: bold;'>データが存在しません。</p>"))