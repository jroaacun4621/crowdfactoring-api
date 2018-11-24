from managers.page_info_manager import PageInfoManager

class PageInfoController:
    @staticmethod
    def get_id(id):
        return PageInfoManager.get_id(id)

    @staticmethod
    def update(id, new_visits):
        PageInfoManager.update(id, new_visits)

    @staticmethod
    def increase_visits(id):
        page_info = PageInfoController.get_id(id)
        new_visits = page_info['visits'] + 1
        PageInfoController.update(id, new_visits)