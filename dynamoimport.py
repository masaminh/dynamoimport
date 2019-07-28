"""jsonファイルの内容をDynamoDBにインポートする."""
import json
from argparse import ArgumentParser, FileType

import boto3
from tqdm import tqdm


def main():
    """メイン関数."""
    p = ArgumentParser(description='jsonファイルの内容をDynamoDBにインポートする')
    p.add_argument('table', help='テーブル名')
    p.add_argument('json', type=FileType('r'), help='インポート内容記載したjsonファイル')
    args = p.parse_args()

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(args.table)
    items = json.load(args.json)

    with table.batch_writer() as batch:
        for item in tqdm(items):
            batch.put_item(Item=item)


if __name__ == "__main__":
    main()
