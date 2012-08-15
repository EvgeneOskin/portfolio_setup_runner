import commands
import os
import os.path

current_path = os.path.abspath(os.curdir)

path_to_qoutes_database = "quotes_database"
path_to_stablePortfolio = "bin"
path_to_csv2sql = "bin"
path_to_csvLoader = "bin"

market_name_csvLoader = "NYSE"
path_to_output_csvLoader = os.path.join(current_path, "csvs")
source_csvLoader = "eoddata"
user_name_csvLoader = os.getenv("EOD_USER", "")
password_csvLoader = os.getenv("EOD_PASSWD", "")

path_to_csv_dir = path_to_output_csvLoader
# the same path will be used for path_to_output_csvLoader
path_to_sql_dir = os.path.join(current_path, "sqls")

path_to_database = os.path.join(current_path, "bin/quotes.db")
type_of_database_prepareDB = "sqlite" 

application_name_addToDB = "sqlite3"

date_period_stablePortfolio = '19900101 20200101'

def main():
    str_for_csvLoader = '%s/csvLoader -M "%s" -O "%s" -S "%s" -U "%s" -P "%s"' % (path_to_csvLoader
                                                                    , market_name_csvLoader
                                                                    , path_to_output_csvLoader
                                                                    , source_csvLoader
                                                                    , user_name_csvLoader
                                                                    , password_csvLoader
    )
    str_for_csv2sql = '%s/csv2sql -I "%s" -O "%s"' % (path_to_csv2sql
                                                , path_to_csv_dir
                                                , path_to_sql_dir
    )
    str_for_quotes_database_prepareDB = 'python2.7 %s/prepareDB.py "/%s" "%s"' % (path_to_qoutes_database
                                                                            , path_to_database
                                                                            , type_of_database_prepareDB
    )
    str_for_quotes_database_addToDB = 'python2.7 %s/addToDB.py "%s" "%s" "%s"' % (path_to_qoutes_database
                                                                        , path_to_sql_dir
                                                                        , path_to_database
                                                                        , application_name_addToDB
    )
    str_for_stablePortfolio = '%s/stablePortfolio -I "%s" -T "%s"' % (path_to_stablePortfolio
                                                                , path_to_database
                                                                , date_period_stablePortfolio
    )
    print str_for_csvLoader
    print commands.getstatusoutput(str_for_csvLoader)[1]
    print str_for_csv2sql
    print commands.getstatusoutput(str_for_csv2sql)[1]
    print str_for_quotes_database_prepareDB
    print commands.getstatusoutput(str_for_quotes_database_prepareDB)[1]
    print str_for_quotes_database_addToDB
    print commands.getstatusoutput(str_for_quotes_database_addToDB)[1]
    print str_for_stablePortfolio
    print commands.getstatusoutput(str_for_stablePortfolio)[1]

if __name__ == "__main__":
    main()