#EXPORT USER USING EXPDP METHOD
 
import os
import sys
import subprocess

def get_env_var():
        a = os.getenv("ORACLE_HOME")
        b = os.getenv("ORACLE_SID")
        c = os.getenv("LD_LIBRARY_PATH")
        print 'The ORACLE_HOME for which export needs to be done is %s ' %a
        print 'The ORACLE_SID for which export needs to be done is %s' %b
        print 'The LD_PATH for which export needs to be done is %s'   %c


def db_exp ():
        #Assigning the variables
        db_user=sys.argv[1]
        db_pass = sys.argv[2]
        db_alias = sys.argv[3]
        schema = sys.argv[4]
        dump_file = sys.argv[5]
        expdp_args = db_user + '/' + db_pass + '@' + db_alias + ' SCHEMAS =' + schema + ' DUMPFILE =' + dump_file + ' DIRECTORY = DATA_PUMP_DIR'
#       db_exp_work = subprocess.Popen(["expdp", expdp_args],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        db_exp_work = subprocess.Popen(["expdp", expdp_args], stdout=subprocess.PIPE )
        if db_exp_work.wait() != 0:
                print "db_export() failed!"
                raise Exception("db_export() failed!")
        print "db_export() end!"


# print help function

def help():
        print "Usage : %s db_user db_pass db_alias schema_to_export dump_file" %sys.argv[0]

if __name__ == '__main__':
        if len(sys.argv) != 6:
                help()
                sys.exit(1)
        get_env_var()
        print "If the variables are correct and you want to proceed [Y/N]"
        output = raw_input()
        if output =='Y':
               db_exp ()
        else:
                sys.exit(1)

