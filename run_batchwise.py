import argparse
import os
from request import get_transliterated

parse = argparse.ArgumentParser()

parse.add_argument("--input", default="eng_to_bengali.txt", type=str,
    help="newline seperated roman sentence for transliteration to native script")
parse.add_argument("--output", default="in_bengali.txt", type=str, 
    help="output filepath")
parse.add_argument("--itc", default="bn-t-i0-und", type=str,
    help="codes can be located https://cloud.google.com/translate/docs/languages")
parse.add_argument("--batch_size", default=100, type=int,
    help="determines batch size default is 100")



def handle_outputs(outputs):
    reformed_outputs = []
    for val in outputs:
        val = eval(val)
        if val[0] != 'SUCCESS':
            reformed_outputs.append('')
            continue
	    
        try:
            reformed_outputs.append(val[1][0][1][0].strip())
        except IndexError:
	        reformed_outputs.append('')
        
    return reformed_outputs

if __name__ == '__main__':
    args = parse.parse_args()
    with open(args.input, 'r') as rf:
        with open(args.output,'w') as wf:
            batch = []
            for line in rf.readlines():
                batch.append(line)
                if len(batch)==args.batch_size:
                    transversion = get_transliterated(batch, args.itc)
                    reformed_outputs = handle_outputs(transversion)
                    full_text = '\n'.join(reformed_outputs)
                    wf.write(full_text)
                    batch = []
            transversion = get_transliterated(batch, args.itc)
            reformed_outputs = handle_outputs(transversion)
            full_text = '\n'.join(reformed_outputs)
            wf.write(full_text)
            

