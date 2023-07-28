import os


def convert_hex_to_text(hex_string):
    try:
        byte_data = bytes.fromhex(hex_string)
        text = byte_data.decode('utf-8')
        return text
    except ValueError:
        return hex_string


# ファイルパス
file_path = "pre_convert_auth_log/auth.log"

# 出力ファイルのディレクトリパス
output_directory = "./ip_logs/"

# ディレクトリが存在しない場合は作成する
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# ファイルを読み込む
with open(file_path, "r") as file:
    # ファイル内の各行を処理する
    for line in file:
        elements = line.split(",")
        ip_address = elements[3].split(".")[0] + "." + elements[3].split(".")[1]  # IPアドレスの2つ目のクラスを取得する
        converted_text = [convert_hex_to_text(element) for element in elements]
        converted_line = ",".join(converted_text)

        # IPアドレスごとのディレクトリを作成する
        ip_log_directory = os.path.join(output_directory, ip_address)
        if not os.path.exists(ip_log_directory):
            os.makedirs(ip_log_directory)

        # IPごとのログファイルに書き込む
        ip_log_file_path = os.path.join(ip_log_directory, f"{ip_address}_log.txt")
        with open(ip_log_file_path, "a") as ip_log_file:
            # 各IPごとのログファイルに変換結果を書き込む
            ip_log_file.write(converted_line + "\n")

        # 全IPのログを格納するディレクトリにもログを書き込む
        all_ips_log_directory = os.path.join(output_directory, "all_ips")
        if not os.path.exists(all_ips_log_directory):
            os.makedirs(all_ips_log_directory)

        all_ips_log_file_path = os.path.join(all_ips_log_directory, "all_ips_log.txt")
        with open(all_ips_log_file_path, "a") as all_ips_log_file:
            # 全IPのログを書き込む
            all_ips_log_file.write(converted_line + "\n")

        # コンソールに変換結果を表示する
        # print(converted_line)
