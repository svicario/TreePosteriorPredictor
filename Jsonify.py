import json
def GuessingModelfromHeader(Header,Model,partitionPlan,mrbayes=True):
    #dictionary matching json with mrbayes names
    sinonimi={'TL':'Tree','kappa':'matrix','r':'matrix','m':'mult','alpha':'gamma','pinvar':'pinv','pi':'States'}
    #dictionary names single parameters matching json with mrbayes names
    nomi={"A<->C":"AC", "A<->G":"AG",'A<->T':"AT",'C<->G':"CG","C<->T":"CT","G<->T":"GT","A":"A","C":"C","T":"T","G":"G"}
    #dictionary mapping the position of each item in the json
    struttura={'Tree':['Tree'],'matrix':["matrix","values"],"mult":["SiteVariation","mult"],'gamma':["SiteVariation", "gamma"],"pinv":["SiteVariation","pinv"],'States':["States","values"]}
    Header=Header.split()
    #coef one is to fit with mrbayes counting that start from one not zero as python
    #exabayes start from zero
    #each time coef appear in this function is to fix the problem
    coef=0
    if mrbayes:
        coef=1
    #Tree order
    SingleTree=True
    Tree_list=[[y,x+coef] for x,y in enumerate([x for x,y in enumerate(Header) if y.find("TL")==0])]
    if len(Tree_list)!=1:
        SingleTree=False
        Tree_dict={}
        Tree_dict.update(Tree_list)    
    partitionPlan=[(str(x+coef),y)for x,y in enumerate(partitionPlan)]
    partitionPlan_dict={}
    partitionPlan_dict.update(partitionPlan)
    partitions=map(str,range(0+coef,coef+len(partitionPlan)))
    place={}
    #loop across partitions
    for p in partitions:
        place[partitionPlan_dict[p]]={"ngen":"@0@"}
        items=[[x,y[:y.find("{")]+y[y.find("}")+1:]] for x,y in enumerate(Header) if p in y[(y.find("{")+1):y.find("}")]]
        items+=[[x,y[:y.find("{")]+y[y.find("}")+1:]] for x,y in enumerate(Header) if "all" in y[(y.find("{")+1):y.find("}")]]
        #items=[[x,y[:y.find("{")]] for x,y in enumerate(Header) if p in y[y.find("{"):]]
        #items+=[[x,y[:y.find("{")]] for x,y in enumerate(Header) if "all" in y[y.find("{"):]]
        #loop across possible parameters accepted by json format
        for k in sinonimi:
            k_items=[[x,y[len(k):]] for x,y in items if y.find(k)==0]
            if k_items:
                temp=place[partitionPlan_dict[p]]
                #loop across pathway in the json for the value
                for kk in struttura[sinonimi[k]][:-1]:
                    try:
                        temp=temp[kk]
                    except KeyError:
                        temp[kk]={}
                        temp=temp[kk]
                last=struttura[sinonimi[k]][-1]
                if last=="Tree":
                    if SingleTree:
                        temp[last]="@{prefix}.run{nrun}.t_pos"+str(k_items[0][0])+"@"
                    else:
                        temp[last]="@{prefix}.tree"+str(Tree_dict[k_items[0][0]])+".run{nrun}.t_pos"+str(Tree_dict[k_items[0][0]])+"@"
                elif last=="values":
                    temp[last]=[]
                    temp["names"]=[]
                    for k_item in k_items:                   
                        temp[last].append("@"+str(k_item[0])+"@")
                        temp["names"].append(nomi[k_item[1][1:-1]])
                else:
                    temp[last]="@"+str(k_items[0][0])+"@"
 
            
    return place

def GettingInfoFromInput(NexusInput):
    shape_dict={"1":"JC","2":"HKY","6":"GTR"}
    "gettinginfo from mrbayes block in nexus"
    #Function assume that datatype is uniform! all DNA, all protein no mix
    from Bio.Nexus.Nexus import Nexus
    N=Nexus()
    N.read(NexusInput)
    MBblock=[x for x in N.unknown_blocks if x.title.lower()=="mrbayes"][0]
    #getting the number of runs
    mcmcCMD=sum([x.split() for x in MBblock.commandlines[0] if x.find("mcmc")==0],[])
    nruns=[int(y.split("=")[-1]) for y in mcmcCMD if y.find("nruns")==0][0]
    #get the matrix size
    lsetCMD=[x for x in MBblock.commandlines[0] if x.lower().find("lset")==0]
    size=[y for y in " ".join(lsetCMD).split() if y.lower().find("nucmodel")==0]
    if len(size)>0:
        size=int(size[0].split("=")[-1])
        size=size_dict[size]
    else:
        size="4X4"
    #get charset information 
    charsets=[" ".join(x.split()[1:])  for x in MBblock.commandlines[0] if x.lower().find("charset")==0]
    ##make a clean dictionary
    Charsets={}
    for charset in charsets:
        k,v=charset.split("=")
        V=[]
        for vv in v.split():
            if vv.find("-"):
                start,end=vv.split("-")
                step=1
                if end.find("\\")>-1:
                    end,step=end.split("\\")
                V+=range(int(start),int(end),int(step))
            else:
                try:
                    #I assume it could be a single site
                    vv=int(vv)
                except ValueError:
                    #it means that this portion of partition is not number but a reference to previously defined partition
                    V+=Charsets[vv]
                else:
                    V.append(vv)
        Charsets[k.strip()]=V
    #get partition information
    partitionPlan=[" ".join(x.split()[1:])  for x in MBblock.commandlines[0] if x.lower().find("partition")==0][0]
    ##make a clean list
    partitionPlan=[x.strip() for x in partitionPlan.split(":")[-1].split(",")]
    #print charsets, partitionPlan
    

    from Bio.Nexus.Nexus import _compact4nexus
    Model={}
    counter=1
    for partition in partitionPlan:
        Model[partition]={"ntaxa":N.ntax,"type":N.datatype,"matrix":{"size":size}}
        if N.datatype.lower()=="dna":
            lsetCMDpart=lsetCMD
            if len(partitionPlan)>1:
                # find lset cmd that refer to correct partition
                #lsetCMD=[x for x in lsetCMD if x(x.find("applyto")>-1)&(counter in map(int,x[:-1].split("{")[-1].split(",")))]
                lsetCMDpart=[]
                for l in lsetCMD:
                    for ll in l.split():
                        if (ll.find("applyto")>-1):
                            ll=ll.strip().split("(")[-1][:-1]
                            if ll=="all":
                                lsetCMDpart.append(l)
                                break                                
                            elif counter in map(int,ll.split(",")) :
                                lsetCMDpart.append(l)
                                break
            print lsetCMDpart
            shape=[y.split("=")[-1].strip() for y in "".join(lsetCMDpart).split() if y.lower().find("nst")==0]
            shape=shape_dict[shape[0]]
        if N.datatype.lower()=="protein":
            prsetCMD=[x for x in MBblock.commandlines[0] if x.lower().find("prset")>-1]
            if len(partitionPlan)>1:
                prsetCMD=[x for x in prsetCMD if (x.find("applyto")>-1)&(counter in map(int,x[:-1].split("{")[-1].split(",")))]
            shape=[y for y in prsetCMD if y.lower().find("aamodelpr")==0]
            shape=shape[0]
            if shape.find("fixed")>-1:
                shape=shape.strip()[5:-1]
        Model[partition]["matrix"]["shape"]=shape
        Model[partition]["partitionSize"]=len(Charsets[partition])
        #this because compact think that number start from zero
        Model[partition]["partitionRange"]=_compact4nexus([x-1 for x in Charsets[partition]])
        counter+=1
    return Model,partitionPlan, nruns

def GettingInfoFromInputExa(prefix):
    ##Getting all files that we need
    import os
    ll=os.listdir("./")
    #I assume that there are only one info file
    info=[x for x in ll if x.find(prefix+"_info")>-1][0]
    handle=open(info,"r")
    print "w",info
    RR=handle.readlines()
    pos=[x for x,y in enumerate(RR) if y.find("ExaBayes was called as follows:")>-1][0]
    call=RR[pos+1]
    print call
    files={}
    key=None
    for i in call.split():
        if key!=None:
            files[key]=i
            key=None
        if i[0]=="-":
            key=i
    print files
    partfile=files["-q"]
    NexusInput=files["-c"]
    MSA=files["-f"]
    ##Parsing partfile
    handle=open(partfile,"r")
    R=handle.readlines()
    handle.close()
    RR=[x.strip().split(",") for x in R]
    RRR=[x[:1]+x[1].split("=") for x in RR]
    partitionPlan=zip(*RRR)[1]
    Model={}
    for p in partitionPlan:
        infopart=[x for x in RRR if x[1]==p][0]
        if infopart[0].upper()=="DNA":
            datatype="DNA"
            size="4X4"
            shape="GTR"
        elif infopart[0].upper()=="PROT":
            datatype="Protein"
            size="20X20"
            shape=None
        elif infopart[0].lower() in proteinModel_dict.keys():
            datatype="Protein"
            size="20X20"
            shape=infopart[0].lower()
        else:
            raise TypeError, "datatype not recognized "+ infopart[0]
        partitionRange=infopart[2]
        #define partitionSize
        #Exabayes does not re-use charset defition
        V=[]
        for vv in partitionRange.split():
            if vv.find("-"):
                start,end=vv.split("-")
                step=1
                if end.find("\\")>-1:
                    end,step=end.split("\\")
                V+=range(int(start),int(end),int(step))
            else:
                #I assume it could be a single site
                vv=int(vv)
                V.append(vv)
        partitionSize=len(V)
        Model[p]={"type":datatype,"partitionSize":partitionSize,"partitionRange":partitionRange,"matrix":{"size":size, "shape":shape}}
    ##Parsing the nexus cmd file
    handle=open(NexusInput,"r")
    R=handle.readlines()
    handle.close()
    bigshape=[x for x in R if x.lower().find("revmatpr")>-1]
    if bigshape:
        Shape=bigshape[0]
        if Shape.find("fixed")>-1:
            shape="GTR"
            values=Shape.strip()[(Shape.find("fixed(")+1):-1]
            values='"'+re.sub(",",'","',values)+'"'
            #I have no idea of names!!!
            for p in Model:
                Model[p]["matrix"]["shape"]=shape
                Model[p]["matrix"]["values"]=values
        elif Shape.find("dirichlet")>-1:
            shape="GTR"
            for p in Model:
                Model[p]["matrix"]["shape"]=shape
    stateFreqPr=[x for x in R if x.lower().find("stateFreqPr")>-1]
    if stateFreqPr:
        stateFreqPr=stateFreqPr[0]
        if stateFreqPr.find("fixed")>-1:
            values=stateFreqPr.strip()[(stateFreqPr.find("fixed(")+1):-1]
            values='"'+re.sub(",",'","',values)+'"'
            #I have no idea of names!!!
            for p in Model:
                Model[p]["States"]["values"]=values
    aaPr=[x for x in R if x.lower().find("aaPr")>-1]
    if aaPr:
       aaPr=aaPr[0]
       if aaPr.find("fixed")>-1:
           shape=aaPr.strip()[(aaPr.find("fixed(")+1):-1]
           for p in Model:
               Model[p]["matrix"]["shape"]=shape
               Model[p]["type"]="Protein"
    nruns=[x for x in R if x.lower().find("numruns")>-1][0]
    nruns=int(nruns.strip().split()[1])
    ##parsing the MSA file
    handle=open(MSA,"r")
    l=[None]
    while len(l)!=2:
        l=handle.readline()
        if l=="": break
        l=l.split()
    print l
    ntaxa=l[0]
    for p in Model:
        Model[p]["ntaxa"]=ntaxa
    return Model, partitionPlan, nruns
    
            
            
        
    
def MrBayes2Json(NexusInput, prefix, burnin, sample, mrbayes=True):
    import json, re
    if mrbayes:
        Model,partitionPlan,nruns=GettingInfoFromInput(NexusInput)
    else:
        print "I assume it is ExaBayes"
        Model,partitionPlan,nruns=GettingInfoFromInputExa(prefix)
    JSONone={"FixedParameters":Model,"VariableParameters":[]}
    for p in range(nruns):
        if mrbayes:
            p+=1
        phandle=open(prefix+".run"+str(p)+".p","r")
        while 1:
            line=phandle.readline()
            if line.find("Gen")==0: break
        Header=line
        place=GuessingModelfromHeader(Header,Model,partitionPlan,mrbayes)
        startpos=phandle.tell()
        f=phandle.readlines()
        ngen=len(f)
        phandle.seek(startpos)
        ngen=ngen-int(burnin)
        step=ngen/int(sample)
        tfile={}
        for part in place:
            place[part]["Tree"]=place[part]["Tree"].format(nrun=p, prefix=prefix)
            try:
                handle=open(place[part]["Tree"][1:-1].split("_pos")[0],"r")
            except IOError:
                treename=place[part]["Tree"][1:-1].split("_pos")[0]
                treename=treename.split(".")
                #ExaBayes have the run and tree part inverted compared to mrbayes
                #here I assume that error happen only when there are more than one tree
                treename=".".join([".".join(treename[:-3]),treename[-2],treename[-3],treename[-1]])
                handle=open(treename,"r")
                
            POS=place[part]["Tree"][1:-1].split("_pos")[-1]
            tfile[POS]={"file":handle,"curLine":None}
            while 1:
                linet=handle.readline()
                if linet.strip().find("tree")==0:
                    break
                bitpos=tfile[POS]["file"].tell()
            tfile[POS]["file"].seek(bitpos)
        print tfile.keys()
        placeString=json.dumps(place)
        placeString=re.split('"*@"*',placeString)
        #Burningout the  Burnin
        for i in range(burnin):
            line=phandle.readline()
            for t in tfile:
                tfile[t]["curLine"]=tfile[t]["file"].readline()
        #Collecting Models
        STEP=0
        while 1:
            STEP+=1
            line=phandle.readline()
            for t in tfile:
                tfile[t]["curLine"]=tfile[t]["file"].readline()
            if line=="":break
            line=line.split()
            if (STEP==step):
                LIST=[]
                STEP=0
                for s in placeString:
                    try:
                        s=int(s)
                    except ValueError:
                        if s.find("_pos")>-1:
                            tree=tfile[s.split("_pos")[-1]]["curLine"]
                            tsplit=tree.split()
                            tree='"'+tsplit[-1]+'"'
                            tgen=tsplit[1].split(".")[1]
                            #ensure that p and t file are in sync
                            assert  int(tgen)== int(line[0])
                            LIST.append(tree)
                        else:
                            LIST.append(s)
                    else:
                        LIST.append(line[s])
                partitionJson=json.loads("".join(LIST))
                JSONone["VariableParameters"].append({"model":partitionJson})
    return JSONone

def findThinning(ngen, burnin, Exsampling):
    """finding the """
    ngen=ngen-int(burnin)
    thinning=ngen/int(Exsampling)
    print samplefreq,ngen, Exsampling,
    return  thinning

if __name__=="__main__":
    import sys
    com={"-P":None,"-j":"prova.json"}
    count=1
    key=None
    for i in sys.argv:
        if key!=None:
            com[key]=i
            key=None
        if i[0]=="-":
            key=i
    spiegazione=""" 
    -j jsonoutput
    -i nexus input
    -p prefix
    -b burnin
    -s sample size 
    -P partitionfile [only for exabayes]
    -m boolean 0 or 1 the input is mrbayes (otherwise exabayes)
    """
    if len(com)<6:
        print spiegazione
    print com
    output=com["-j"]
    NexusInput=com["-i"]
    
    JJ=MrBayes2Json(NexusInput, prefix=com["-p"], burnin=int(com["-b"]), sample=int(com["-s"]), mrbayes=bool(int(com["-m"])))
    JJstring=json.dumps(JJ)
    handle=open(output,"w")
    handle.write(JJstring)
    handle.close()
