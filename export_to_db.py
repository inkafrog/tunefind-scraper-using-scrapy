import dataset
import json_lines

from tunefind.settings import DB_SETTINGS, JSON_FILE_NAME


def export_to_database(tbl):
    _db = DB_SETTINGS
    db = dataset.connect(f"mysql://{_db['user']}:{_db['password']}@{_db['host']}:{_db['port']}/{_db['db']}?charset=utf8mb4")
    table = db[tbl]
    with open(JSON_FILE_NAME, 'rb') as f:
        for item in json_lines.reader(f):
            url = item.get("url")
            data_to_insert = {
                "url": url,
                "song_titles": '|'.join(item.get("song_titles")),
                "song_sub_titles": '|'.join(item.get("song_titles")),
                "event_titles": '|'.join(map(lambda x: x.get('title'), item.get("events"))),
                "event_description": '|'.join(map(lambda x: x.get('description'), item.get('events'))),
                "event_date": '|'.join(map(lambda x: x.get('date'), item.get('events'))),
                "event_link_url": '|'.join(map(lambda x: x.get("link")['url'], item.get('events'))),
                "event_link_text": '|'.join(map(lambda x: x.get("link")['text'], item.get('events'))),
            }
            if table.find_one(url=url):
                continue

            print('inserting info of:', url)
            table.insert(data_to_insert)


if __name__ == '__main__':
    table_name = 'tunefind'
    export_to_database(table_name)
