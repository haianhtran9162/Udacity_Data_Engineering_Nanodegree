from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self, table="", redshift_conn_id="", query="", *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.query = query

    def execute(self, context):
        self.log.info("LoadFactOperator is starting ...")
        self.log.info("Starting connect to DB...")
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        self.log.info(f"Insert data into the table {self.table}...")
        redshift.run(f"INSERT INTO {self.table} {self.query}")
        self.log.info("Done.")