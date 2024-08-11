from models import Authors, Qoutes
import connect

def search_by_author(author_name):
    author = Authors.objects(fullname=author_name).first()
    if author:
        quotes = Qoutes.objects(author=author)
        return [quote.quote for quote in quotes]
    return []


def search_by_tag(tag_name):
    quotes = Qoutes.objects(tags__name=tag_name)
    return [quote.quote for quote in quotes]


def search_by_tags(tag_names):
    tags_list = tag_names.split(',')
    quotes = Qoutes.objects(tags__name__in=tags_list)
    return [quote.quote for quote in quotes]


def main():
    while True:
        command = input("Enter command: ").strip()

        if command.startswith("name:"):
            author_name = command.split(":", 1)[1].strip()
            results = search_by_author(author_name)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        elif command.startswith("tag:"):
            tag_name = command.split(":", 1)[1].strip()
            results = search_by_tag(tag_name)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        elif command.startswith("tags:"):
            tag_names = command.split(":", 1)[1].strip()
            results = search_by_tags(tag_names)
            for result in results:
                print(result.encode('utf-8').decode('utf-8'))

        elif command == "exit":
            print("Exiting...")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()