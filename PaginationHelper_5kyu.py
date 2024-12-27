class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        if self.items_per_page <= 0:
            return 0
        number_of_pages = len(self.collection) // self.items_per_page
        if len(self.collection) % self.items_per_page > 0:
            number_of_pages += 1

        return number_of_pages

    def page_item_count(self, page_index):
        number_of_pages = self.page_count()
        total_items = len(self.collection)

        if page_index < 0 or page_index >= number_of_pages:
            return -1

        start_index = page_index * self.items_per_page

        remaining_items = total_items - start_index

        if remaining_items < self.items_per_page:
            return remaining_items

        return self.items_per_page
#always check this one(had some problems with it)
    def page_index(self, item_index):
        if ((item_index / self.items_per_page) < 1) and (item_index >= 0) and (len(self.collection) > 0) and (
                item_index < len(self.collection)):
            return 0
        elif ((item_index / self.items_per_page) >= 1) and (
                (item_index / self.items_per_page) < self.page_count()) and (item_index > 0) and (
                (len(self.collection) > 0)) and (item_index < len(self.collection)):
            return item_index // self.items_per_page
        else:
            return -1
