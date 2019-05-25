import re


class PSQLtoSparkSQLTranslator(object):
    
    def __init__(self):
        pass

    def translate(self, text):
        text = self._replace_quotes(text)
        return text

    @staticmethod
    def _replace_quotes(text):
        return re.sub("\"", "`", text)

    @staticmethod
    def _replace_date_funcs(text):
        return text

    @staticmethod
    def _replace_miscs(text):
        return text


if __name__ == "__main__":

    text = """
    SELECT distinct
    "zone_id", 
    split_part("model_scope_id", '|', 2) as zone_bucket
    FROM "KIL_SCOPE_scope_metadata"
    where split_part("model_scope_id", '|', 2) is not null
    """
    print(PSQLtoSparkSQLTranslator().translate(text))