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
        items=[]
        for x,y in enumerate(Header):
            base=y[(y.find("{")+1):y.find("}")]
            if base=="":
                items.append([x,y])
            base=base.split(",")
            for b in base:
                if b.find("-")>-1:
                    start,end=map(int,b.split("-"))
                    b=map(str,range(start,end+1))
                else:
                    b=[b]
                for bb in b:
                    if b=="all" or bb==p:
                        items.append([x,y[:y.find("{")]+y[y.find("}")+1:]])
        #loop across possible parameters accepted by json format
        for k in sinonimi:
            k_items=[[x,y[len(k):]] for x,y in items if (y.find(k)==0) and ( len(k)==len(y) or y.find("(")==len(k))]
            #print k,k_items
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
                        if not mrbayes:
                            temp[last]="@ExaBayes_topologies.{prefix}.{nrun}_pos"+str(k_items[0][0])+"@"
                    else:
                        temp[last]="@{prefix}.tree"+str(Tree_dict[k_items[0][0]])+".run{nrun}.t_pos"+str(Tree_dict[k_items[0][0]])+"@"
                        if not mrbayes:
                            temp[last]="@ExaBayes.run{nrun}.tree"+str(Tree_dict[k_items[0][0]])+".t_pos"+str(Tree_dict[k_items[0][0]])+"@"
                            
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
    size_dict={"4by4":"4X4","doublet":"16X16","codon":"64X64"}
    "gettinginfo from mrbayes block in nexus"
    #Function assume that datatype is uniform! all DNA, all protein no mix
    from Bio.Nexus import Nexus
    N=Nexus.Nexus()
    N.read(NexusInput)
    #merging togheter all possible mrbayes block present in the file as a long list of command
    #should I take only the first one?
    cmdblock=sum([sum(x.commandlines,[]) for x in N.unknown_blocks if x.title.lower()=="mrbayes"],[])
    HyppartitionPlan={}
    partitionPlan=["dummy"]
    
    for cmdline in cmdblock:
        CMDline=Nexus.Commandline(cmdline,"mrbayes")
        if CMDline.command=="charset":
            N._charset(CMDline.options)
        elif CMDline.command=="partition":
            nameplan=cmdline.split("=")[0].split()[1]
            HyppartitionPlan[nameplan]=[x.strip() for x in cmdline.split(":")[-1].split(",")]
        elif CMDline.command.find("mcmc")>-1:
            try:
                nruns=CMDline.options["nruns"]
            except KeyError:
                pass
        elif CMDline.command=="set":
            if CMDline.options.has_key("partition"): 
                partitionPlan=HyppartitionPlan[CMDline.options["partition"]]
    #print cmdblock
    #print partitionPlan
    Model={}
    counter=1
    for partition in partitionPlan:
        Model[partition]={"ntaxa":N.ntax,"type":N.datatype.lower().title(),"matrix":{}}
        Model[partition]["partitionSize"]=len(N.charsets[partition])
        Model[partition]["partitionRange"]=Nexus._compact4nexus(N.charsets[partition])
        for cmdline in cmdblock:
            CMDline=Nexus.Commandline(cmdline,"mrbayes")
            if N.datatype.lower()=="dna":
                if CMDline.command=="lset":
                    test1=test2=test3=False
                    if CMDline.options.has_key("applyto"):
                        APP=CMDline.options["applyto"][1:-1].lower()
                        if (APP.strip()=="all"):
                            test2=True
                        elif counter in map(int,APP.split(",")):
                            test3=True
                    else:
                        test1=True
                    if test1 or test2 or test3:
                        Model[partition]["matrix"]["shape"]=shape_dict[CMDline.options["nst"]]
                        if CMDline.options.has_key("nucmodel"):
                            Model[partition]["matrix"]["size"]=size_dict(CMDline.options["nucmodel"])
                        else:
                            Model[partition]["matrix"]["size"]="4X4"
            if N.datatype.lower()=="protein":
                Model[partition]["matrix"]["size"]="20X20"
                if CMDline.command=="prset":
                    mod=CMDline.options["aamodelpr"]
                    if mod.find("fix")>-1:
                       Model[partition]["matrix"]["shape"]=mod[(mod.find("(")+1):(mod.find(")")-1)]
                    elif mod.find("(")==-1:
                       Model[partition]["matrix"]["shape"]=mod 

        counter+=1    

    return Model,partitionPlan, int(nruns)

def GettingInfoFromInputExa(prefix, aln):
    ##Getting all files that we need
    import os
    from Bio import AlignIO
    ll=os.listdir("./")
    #I assume that there are only one info file
    info=[x for x in ll if x.lower().find("exabayes_info."+prefix.lower())>-1][0]
    handle=open(info,"r")
    print "InfoFile",info
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
    if aln:
        files["-f"]=aln
    print files
    NexusInput=files["-c"]
    MSA=files["-f"]
    if files.has_key("-q"):
        ##Parsing partfile
        partfile=files["-q"]
        handle=open(partfile,"r")
        R=handle.readlines()
        handle.close()
        RR=[x.strip().split(",") for x in R]
        RRR=[x[:1]+x[1].split("=") for x in RR]
        partitionPlan=zip(*RRR)[1]
    else:
        partitionPlan=["dummy"]
        a=AlignIO.read(MSA,"phylip")
        infopart=[files["-m"],"dummy","1-"+str(len(a))]

    Model={}
    for p in partitionPlan:
        if files.has_key("-q"):
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
    
            
            
        
    
def MrBayes2Json(NexusInput, prefix, burnin, sample, mrbayes=True, aln=None):
    import json, re
    if mrbayes:
        Model,partitionPlan,nruns=GettingInfoFromInput(NexusInput)
    else:
        print "I assume it is ExaBayes"
        Model,partitionPlan,nruns=GettingInfoFromInputExa(prefix, aln)
        if not prefix:
            prefix="ExaBayes"
    JSONone={"FixedParameters":Model,"VariableParameters":[]}
    for p in range(nruns):
        if mrbayes:
            p+=1
        try:
            phandle=open(prefix+".run"+str(p)+".p","r")
        except IOError:
            try:
                phandle=open("ExaBayes_parameters."+prefix+"."+str(p),"r")
            except IOError:
                phandle=open("ExaBayes.run"+str(p)+".p","r")
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
        step=round(ngen/int(sample))
        if step==0:
            step=1
        print step
        tfile={}
        for part in place:
            #print p,part, place[part]
            place[part]["Tree"]=place[part]["Tree"].format(nrun=p, prefix=prefix)
            handle=open(place[part]["Tree"][1:-1].split("_pos")[0],"r")
##            try:
##                handle=open(place[part]["Tree"][1:-1].split("_pos")[0],"r")
##            except IOError:
##                treename=place[part]["Tree"][1:-1].split("_pos")[0]
##                treename=treename.split(".")
##                #ExaBayes have the run and tree part inverted compared to mrbayes
##                #here I assume that error happen only when there are more than one tree
##                treename=".".join([".".join(treename[:-3]),treename[-2],treename[-3],treename[-1]])
##                handle=open(treename,"r")                
            POS=place[part]["Tree"][1:-1].split("_pos")[-1]
            tfile[POS]={"file":handle,"curLine":None}
            while 1:
                linet=handle.readline()
                if linet.strip().find("tree")==0:
                    break
                bitpos=tfile[POS]["file"].tell()
            tfile[POS]["file"].seek(bitpos)
        #print tfile.keys()
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
    com={"-i":None,"-p":None,"-j":"prova.json"}
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
    -a alignment in phylip format (for exabayes in case the exabayes call was done using binary alignment)
    -p namerun
    -b burnin
    -s sample size 
    -m boolean 0 or 1 the input is mrbayes (otherwise exabayes)
    """
    if len(com)<6:
        print spiegazione
    print com
    output=com["-j"]
    JJ=MrBayes2Json(NexusInput=com["-i"], prefix=com["-p"], burnin=int(com["-b"]), sample=int(com["-s"]), mrbayes=bool(int(com["-m"])), aln=com["-a"])
    JJstring=json.dumps(JJ, sort_keys=True,indent=4, separators=(',', ': '))
    handle=open(output,"w")
    handle.write(JJstring)
    handle.close()
