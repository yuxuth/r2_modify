import gzip
from argparse import ArgumentParser

def update_fastq(r1, out_r1 ): ## process two files

    
    f_r1 = gzip.open(r1, 'rt')
    f_out_r1 = open(out_r1, 'w')


    while True:
        cur_r1_name = f_r1.readline()
        cur_r1_read = f_r1.readline().strip()
        cur_r1_plus = f_r1.readline()
        cur_r1_qual = f_r1.readline().strip()
        

    
        if cur_r1_name == "" : break
        
#         if not (cur_r1_name.split('/')[0] == cur_r2_name.split()[0] ):
#             sys.exit("error: read name does not match")
            
     
        cur_r1_name = cur_r1_name.replace("/2","/1")
        
        
        f_out_r1.write(cur_r1_name)
        f_out_r1.write(cur_r1_read+"\n")
        f_out_r1.write(cur_r1_plus)
        f_out_r1.write(cur_r1_qual+"\n")     
    
   
    f_r1.close()

    f_out_r1.close()

def main():
    parser = ArgumentParser(description='provide fastq and new files') ## add parser
    parser.add_argument('-r1', help='r1', required=True)
    # parser.add_argument('-r2',  help='r2', required=True)
    parser.add_argument('-o',  help='file_name', required=True)
    options = parser.parse_args()
    r1 = options.r1
    #FASTQ_R2 = options.r2 ## assume all file from BGI
    # FASTQ_R2 = FASTQ_R1.replace('_1.fq.gz','_2.fq.gz')
    out_r1 = options.o

    update_fastq(r1, out_r1)

if __name__== "__main__":
    main()
