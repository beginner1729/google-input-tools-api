import argparse
import os
from request import get_transliterated

parse = argparse.ArgumentParser()

parse.add_argument("--input", default="eng_to_bengali.txt", type=str,
    help="newline seperated roman sentence for transliteration to native script")
parse.add_argument("--output", default="in_bengali.txt", type=str, 
    help="output filepath")
parse.add_argument("--itc", default="bn", type=str,
    help="codes can be located https://cloud.google.com/translate/docs/languages")
parse.add_argument("--batch_size", default=100, type=int,
    help="determines batch size default is 100")



def handle_outputs(batch, outputs):
    reformed_outputs = []
    total_trans = []
    for val in outputs:
        val = eval(val)
        trans = val[1][0][0]
        if val[0] != 'SUCCESS':
            reformed_outputs.append(','.join([trans,' ']))
            continue
	    
        try:
            v_edited = val[1][0][1][0].strip()
            reformed_outputs.append(','.join([trans,v_edited]))
        except IndexError:
	        reformed_outputs.append(','.join([trans,' ']))
        total_trans.append(trans)
    missed = set(batch).difference(set(total_trans))
    if len(missed) > 0:
        print("missed translation are")
        print(missed)
    return reformed_outputs

if __name__ == '__main__':
    args = parse.parse_args()
    with open(args.input, 'r') as rf:
        with open(args.output,'w') as wf:
            wf.write('romanWord,nativeWord\n')
            batch = []
            for line in rf.read().split('\n'):
                if len(line)>0:
                    batch.append(line)
                if len(batch)==args.batch_size:
                    transversion = get_transliterated(batch, args.itc)
                    reformed_outputs = handle_outputs(batch, transversion)
                    full_text = '\n'.join(reformed_outputs)
                    wf.write(full_text)
                    wf.write("\n")
                    batch = []
            transversion = get_transliterated(batch, args.itc)
            reformed_outputs = handle_outputs(batch, transversion)
            full_text = '\n'.join(reformed_outputs)
            wf.write(full_text)
            

