import pandas as pd
import sys
import os

def main(input_path, output_path):
    arealist = pd.read_csv("arealist.csv")
    data = pd.read_csv(input_path)

    arealist = arealist[['area_id', 'area_name', 'area_block']]
    data.rename(columns={'area': 'area_name'}, inplace=True)

    # ファイルサイズ削減のためarea_nameをarea_idで置換
    merged_data = pd.merge(data, arealist, on='area_name', how='left', suffixes=('', ''))

    final_data = merged_data.copy()[['area_id', 'name', 'lat', 'long', 'status', 'note']]

    area_blocks = {
        'akishima-hokusei': '昭島-北西部',
        'akishima-hokutou': '昭島-北東部',
        'akishima-nansei': '昭島-南西部',
        'akishima-nantou': '昭島-南東部',

        'taito-ku': '台東区',        
        'sumida-ku': '墨田区',        
        'koutou-ku': '江東区',        
        'adachi-ku': '足立区',        
        'edogawa-ku': '江戸川区',        
        'katsushika-ku': '葛飾区',        
        'arakawa-ku': '荒川区',        

        'shinagawa-ku': '品川区',        
        'meguro-ku': '目黒区',        
        'ohta-ku': '大田区',        
        'setagaya-ku': '世田谷区',        
        'nakano-ku': '中野区',        
        'suginami-ku': '杉並区',        
        'nerima-ku': '練馬区',        
        'itabashi-ku': '板橋区',        
        'kita-ku': '北区',        

        'chiyoda-ku': '千代田区',        
        'tyuou-ku': '中央区',        
        'minato-ku': '港区',        
        'shinjuku-ku': '新宿区',        
        'bunkyo-ku': '文京区',        
        'shibuya-ku': '渋谷区',        
        'toyoshima-ku': '豊島区',

		'hachiouji': '八王子市',
		'tachikawa': '立川市',
		'musashino': '武蔵野市',
		'mitaka': '三鷹市',
		'oume': '青梅市',
		'fuchu': '府中市',
		'akishima1': '昭島市1',
		'akishima2': '昭島市2',
		'akishima3': '昭島市3',
		'akishima4': '昭島市4',
		'akishima5': '昭島市5',
		'akishima6': '昭島市6',
		'akishima7': '昭島市7',
		'akishima8': '昭島市8',
		'akishima9': '昭島市9',
		'akishima10': '昭島市10',
		'akishima11': '昭島市11',
		'akishima12': '昭島市12',
		'akishima13': '昭島市13',
		'akishima14': '昭島市14',
		'akishima15': '昭島市15',
		'akishima16': '昭島市16',
		'akishima17': '昭島市17',
		'akishima18': '昭島市18',
		'akishima19': '昭島市19',
		'akishima20': '昭島市20',
		'machida': '町田市',
		'koganei': '小金井市',
		'kodaira': '小平市',
		'hino': '日野市',
        'nishitokyo': '西東京市',        

		'nishitama': '西多摩',
		'minamitama': '南多摩',
		'kitatama1': '北多摩第一',
		'kitatama2': '北多摩第二',
		'kitatama3': '北多摩第三',
		'kitatama4': '北多摩第四',
    }
    
    for block_key, block_name in area_blocks.items():
        block_areas = arealist[arealist['area_block'] == block_name]['area_id']
        filtered_data = final_data[final_data['area_id'].isin(block_areas)]
        
        filtered_output_path = os.path.join(output_path, 'block', f'{block_key}.json')
        filtered_data.to_json(filtered_output_path, orient='records', force_ascii=False)
        print(f"Filtered file saved to {filtered_output_path}")

    json_output_path = os.path.join(output_path, 'all.json')
    final_data.to_json(json_output_path, orient='records', force_ascii=False)
    print(f"File saved to {json_output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    main(input_path, output_path)
