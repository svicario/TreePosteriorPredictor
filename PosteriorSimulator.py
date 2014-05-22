InputCodon="""
2          * 0,1:seqs or patters in paml format (mc.paml); 2:paup format (mc.nex)
{random}       * random number seed (odd number)
{nseq} {size} {rep}   * <# seqs>  <# codons>  <# replicates>

{TL}         * <tree length; see note below; use -1 if tree below has absolute branch lengths>
{tree}

{omega}         * omega
{kappa}           * kappa

{codon_frequency_16rows}

{genetic_code}           * genetic code (0:universal; 1:mammalian mt; 2-10:see below)

// end of file.

============================================================================
Change values of parameters, but do not delete them.  You can add
empty lines, but do not break one line into several lines.

Note that tree length and branch lengths under the codon model are
measured by the expected number of nucleotide substitutions per codon
(see Goldman & Yang 1994).  For amino acid models, they are defined as
the expected number of amino acid changes per amino acid site.

64 codon freqs are in fixed order TTT, TTC, TTA, TTG, TCT, TCC, ..., GGG, 
from abglobin.nuc under the F3x4 table


* Genetic codes: 0:universal, 1:mammalian mt., 2:yeast mt., 3:mold mt.,
* 4: invertebrate mt., 5: ciliate nuclear, 6: echinoderm mt., 
* 7: euplotid mt., 8: alternative yeast nu. 9: ascidian mt., 
* 10: blepharisma nu., 11: Yang's regularized code
* These codes correspond to transl_table 1 to 11 of GenBank.

=================!! Check screen output carefully!! ========================
"""

InputAA="""
 2        * 0: paml format (mc.paml); 1:paup format (mc.nex)
{random}       * random number seed (odd number)

{nseq} {size} {rep}  * <# seqs>  <# sites>  <# replicates>

{TL}         * <tree length, use -1 if tree below has absolute branch lengths>

{tree}

{alpha} {cat}        * <alpha; see notes below>  <#categories for discrete gamma>
{matrix_shape} {matrix_file} * <model> [aa substitution rate file, need only if model=2 or 3]

{aa_freq_2rows}  

 A R N D C Q E G H I
 L K M F P S T W Y V

// end of file

=============================================================================
Notes for using the option in evolver to simulate amino acid sequences. 
Change values of parameters, but do not delete them.  It is o.k. to add 
empty lines, but do not break down the same line into two or more lines.

  model = 0 (poisson), 1 (proportional), 2 (empirical), 3 (empirical_F)
  Use 0 for alpha to have the same rate for all sites.
  Use 0 for <#categories for discrete gamma> to use the continuous gamma
  <aa substitution rate file> can be dayhoff.dat, jones.dat, and so on.
  <aa frequencies> have to be in the right order, as indicated.
=================!! Check screen output carefully!! =====================
"""

InputBase="""
 2        * 0: paml format (mc.paml); 1:paup format (mc.nex)
{random}   * random number seed (odd number)

{nseq} {size} {rep}  * <# seqs>  <# nucleotide sites>
{TL}                  * <tree length, use -1 if tree below has absolute branch lengths>

{tree}

{matrix_shape}        * model: 0:JC69, 1:K80, 2:F81, 3:F84, 4:HKY85, 5:T92, 6:TN93, 7:REV
{matrix_param}                    * kappa or rate parameters in model
{alpha} {cat}     * <alpha>  <#categories for discrete gamma>

{base_freq}    * base frequencies
  T        C        A        G


==================================================
The rest of this data file are notes, ignored by the program evolver.
Change the values of the parameters, but do not delete them.
evolver simulates nucleotide sequences under the REV+Gamma model
and its simpler forms.

More notes:
  Parameter kappa or rate parameters in the substituton model: 
    For TN93, two kappa values are required, while for REV, 5 values
    (a,b,c,d,e) are required (see Yang 1994 for the definition of these
    parameters).  
    The kappa parameter is defined differently under HKY85 (when k=1 means
    no transition bias) and under F84 (when k=0 means no bias).
    JC69 and F81 are considered species cases of HKY85, so use 1 for kappa
    for those two models.  Notation is from my two papers in JME in 1994.
  
  Use equal base frequencies (0.25) for JC69 and K80.
  Use 0 for alpha to have the same rate for all sites.
  Use 0 for <#categories for discrete gamma> to use the continuous gamma

=========!! Check screen output carefully !! =====
"""

Json="""
{
"FixedParam":{
	    "partition1":{"partitionSize":201,"type":"DNA","ntaxa":23,"States":{"names":["A","C","G","T"]}},
	    "partition2":{"partitionSize":301,"type":"DNA","ntaxa":23, "matrix":{"names":["AC","AG","AT", "CG","GT","CT"]}},
	    "partition3":{"partitionSize":150,"type":"Protein","ntaxa":23}
	},
"Posterior":[
            {
            "generation":1,
            "model":{
               "partition1":{
                   "matrix":{
                       "size":"4X4","shape":"HKY","values":[1.0] 
                       },
                   "SiteVariation":{
                        "gamma":2,"pinv":3, "mult":5
                        },
                    "States":{
                        "values":[12.0,13.0,14.0,15.0]
                        },
                    "Tree":"((10:0.374133, (((4:0.160982, (1:0.087132, (2:0.021540, 3:0.120324):0.020074):0.025819):0.149324, (5:0.027272, (6:0.012958, 7:0.000004):0.121808):0.084640):0.065240, (8:0.125552, 9i:0.244540):0.051583):0.144918):0.486111, 25:0.663061, ((17:0.234149, (24:0.058237, 2:0.020525):0.334993):0.240316, (22:0.312525, ((18:0.472270, ((11:0.092730, (12:0.138938,13:0.119054):0.108101):0.033261, (14:0.355657, (15:0.013220, 16:0.000004):0.111819):0.134771):0.067821):0.092337, ((19:0.188489, 21:0.364843):0.152098, 20:0.391480):0.116734):0.032322):0.045795):0.265032);"
                    },
                "partition2":{
                    "matrix":{
                      "size":"4X4","shape":"GTR","values":[6.0,7.0,8.0,9.0,10.0,1.0]
                      },
               "SiteVariation":{
                "gamma":3.0,"pinv":4.0, "mult":8.0
                },
                    "States":{
                        "names":["A","C","G","T"],"values":[12.0,13.0,14.0,15.0]
                        },
                    "Tree":"((10:0.374133, (((4:0.160982, (1:0.087132, (2:0.021540, 3:0.120324):0.020074):0.025819):0.149324, (5:0.027272, (6:0.012958, 7:0.000004):0.121808):0.084640):0.065240, (8:0.125552, 9i:0.244540):0.051583):0.144918):0.486111, 25:0.663061, ((17:0.234149, (24:0.058237, 2:0.020525):0.334993):0.240316, (22:0.312525, ((18:0.472270, ((11:0.092730, (12:0.138938,13:0.119054):0.108101):0.033261, (14:0.355657, (15:0.013220, 16:0.000004):0.111819):0.134771):0.067821):0.092337, ((19:0.188489, 21:0.364843):0.152098, 20:0.391480):0.116734):0.032322):0.045795):0.265032);"
                 },
                 "partition3":{
                       "matrix":{
                          "size":"20X20","shape":"WAG"
                         },
                        "SiteVariation":{
                            "gamma":16.0, "mult":11.0
                        },
                      "Tree":"((10:0.374133, (((4:0.160982, (1:0.087132, (2:0.021540, 3:0.120324):0.020074):0.025819):0.149324, (5:0.027272, (6:0.012958, 7:0.000004):0.121808):0.084640):0.065240, (8:0.125552, 9i:0.244540):0.051583):0.144918):0.486111, 25:0.663061, ((17:0.234149, (24:0.058237, 2:0.020525):0.334993):0.240316, (22:0.312525, ((18:0.472270, ((11:0.092730, (_12_H._scalaris:0.138938, _13_H._laevigata:0.119054):0.108101):0.033261, (_14_H._cyclobates:0.355657, (_15_H._rubra:0.013220, _16_H._conicopora:0.000004):0.111819):0.134771):0.067821):0.092337, ((19:0.188489, 21:0.364843):0.152098, 20:0.391480):0.116734):0.032322):0.045795):0.265032); "
                   }
            }}
]}


"""
def transpose(m):
    if isinstance(m, list):
        if isinstance(m[0], list):
            return map(list, zip(*m))
        else:
            return zip(*m) # faster
    else:
        if isinstance(m[0], list):
            return tuple(map(list, zip(*m)))
        else:
            return tuple( zip(*m) )

import sys
from  random import random
import json, os, numpy
#Info to deal with Evolver of Paml
##Base order 
bases=['T', 'C', 'A', 'G']
##Making order index for bases
I=[[base,order] for order,base in enumerate([x for x in bases])]
Bases={}
Bases.update(I)
##Making order index for Codons
Codons={}
I=[[codon,order] for order,codon in enumerate([x+y+z for x in base for y in base for z in base])]
Codons.update(I)
##Dict of all ordered states
State_Order={"20X20":{"A":1, "R":2, "N":3, "D":4, "C":5, "Q":6, "E":7, "G":8, "H":9, "I":10,"L":11, "K":12, "M":13, "F":14, "P":15, "S":16, "T":17, "W":18 ,"Y":19, "V":20},
            "4X4":Bases,
            "16X16":None,
            "64X64":Codons
            }
##order within 4X4 matrix, notice that only GTR and TN93 requires some order and TN93 not supported in mrBayes 
matrix_order={ "6":None, "7": {"CT":1,"TC":1,"AT":2,"TA":2,"TG":3,"GT":3,"CA":4,"AC":4,"CG":5,"GC":5, "AG":6,"GA":6}}
##code name in evolver for the different matrix shape
matrix_dict={"JC69":"0","JC":"0", "K80":"1", "F81":"2", "F84":"3", "HKY85":"4","HKY":"4", "T92":"5", "TN93":"6", "REV":"7","GTR":"7"}
size_dict={"4by4":"4X4","doublet":"16X16","codon":"64X64"}
##protein model
proteinModel_dict={"cprev10":"cpREV10.dat",
                   "dayhoff":"dayhoff.dat",
                   "lg":"lg.dat",
                   "mtrev24":"mtREV24.dat",
                   "cprev64":"cpREV64.dat",
                   "grantham":"grantham.dat",
                   "miyata":"miyata.dat",
                   "mtmama":"mtmam.dat",
                   "vt":"vtMrBayes.dat",
                   "mtzoa":"MtZoa.dat",
                   "jones-dcmut":"jones-dcmut.dat",
                   "wag":"wag.dat",
                   "blosum":"blosumMrBayes.dat",
                   "dayhoff-dcmut":"dayhoff-dcmut.dat",
                   "jones":"jones.dat",
                   "mtart":"mtArt.dat",
                   "mrrev":"mtrev24MrBayes.dat"}

#Reordering of parameters
##Reorder and normalize if necessary frequency of transition parameter and states
def MValue_reformat(values,names,shape):
    order=[matrix_order[shape][n] for n in names]
    IN=zip(order,values)
    IN.sort()
    Values=[x[1] for x in IN]          
    Values=[str(float(x)/float(Values[-1])) for x in Values[:-1]]
    return " ".join(Values)


def StatesValue_reformat(values,names,size):
    order=[State_Order[size][n] for n in names]
    IN=zip(order,values)
    IN.sort()
    Values=[x[1] for x in IN]
    return " ".join(map(str,Values))

#extract the useful parameters from the json
def GeneralFormat(PartitionJson):
    """parameters present in all model for all data types"""
    R=1+int(random()*200000)/2
    rep=PartitionJson["replicates"]
    size=PartitionJson["partitionSize"]
    nseq=PartitionJson["ntaxa"]
    try:
        TL=PartitionJson["SiteVariation"]["mult"]
    except KeyError:
        TL=-1
    tree=PartitionJson["Tree"]
    try:
        alpha=PartitionJson["SiteVariation"]["gamma"]
    except KeyError:
        alpha=0
    try:
        cat=PartitionJson["SiteVariation"]["gamma_categories"]
    except KeyError:
        cat=4
    else:
        if cat=="continuous":
            cat=0
    return {"random":R,"size":size,"nseq":nseq,"TL":TL,"alpha":alpha,"cat":cat, "tree":tree,"rep":rep}

def ProteinFormat(PartitionJson):
    """parameters present in model for Protein data type and 20X20 matrix"""
    if PartitionJson["matrix"]["shape"]=="poisson":
        matrix_shape="0"
    elif PartitionJson["matrix"]["shape"]=="proportional":
        matrix_shape="1"
    else:
        matrix_shape="2"
        #all model name are in lower case within the dict
        path=os.path.dirname(os.path.realpath(__file__))+os.path.sep+"dat"+os.path.sep
        matrix_file=path+proteinModel_dict[PartitionJson["matrix"]["shape"].lower()]
    aa_freq_2rows=""
    try:
        freq=PartitionJson["States"]["values"]
    except KeyError:
        pass
    else:
        matrix_shape="3"
        aa_freq_2rows=StatesValue_reformat(names=PartitionJson["States"]["names"],values=PartitionJson["States"]["values"],size=PartitionJson["matrix"]["size"])
        aa_freq_2rows=" ".join(aa_freq_2rows[:11])+"\n"+" ".join(aa_freq_2rows[11:])
    return {"matrix_shape":matrix_shape,"matrix_file":matrix_file,"aa_freq_2rows":aa_freq_2rows}
def CodonFormat(PartitionJson):
    """parameters present in model for Nucleotide data type and 64X64 matrix"""
    pass

def DoubletFormat(PartitionJson):
    """parameters present in model for Nucleotide data type and 16X16 matrix"""
    pass
def NucleotideFormat(PartitionJson):
    """parameters present in model for Nucleotide data type and 4X4 matrix"""
    base_freq=StatesValue_reformat(size=PartitionJson["matrix"]["size"],**PartitionJson["States"])

    matrix_shape=matrix_dict[PartitionJson["matrix"]["shape"]]
    #print PartitionJson["matrix"]["size"], matrix_shape
    if  matrix_shape=="7":
        matrix_param=MValue_reformat(shape=matrix_shape,values=PartitionJson["matrix"]["values"],names=PartitionJson["matrix"]["names"])
    else:
        matrix_param=PartitionJson["matrix"]["values"]
    return {"matrix_param":matrix_param, "base_freq":base_freq,"matrix_shape":matrix_shape}

def InformPartitionJson(PartitionJson,FixedParamJson):
    """add item to a dictionary including item within a dictionary in a dictionary"""
    for k in FixedParamJson:
        if PartitionJson.has_key(k):
            if FixedParamJson[k].__class__=={}.__class__:
                PartitionJson[k]=InformPartitionJson(PartitionJson[k], FixedParamJson[k])          
        else:
            PartitionJson[k]=FixedParamJson[k]
    return PartitionJson

def InformPartitionJson(PartitionJson,FixedParamJson):
    """add item to a dictionary including item within a dictionary in a dictionary"""
    for k in FixedParamJson:
        if FixedParamJson.__class__=={}.__class__:
            if PartitionJson.has_key(k):
                PartitionJson[k]=InformPartitionJson(PartitionJson[k], FixedParamJson[k])          
            else:
                PartitionJson[k]=FixedParamJson[k]
        elif FixedParamJson.__class__==[].__class__:
            if PartitionJson[0].__class__=={}.__class__:
                if(PartitionJson[0].has_key["TreeLink"] and FixedParamJson[0].has_key("Treelink")):
                    order,Partition_k=[(y,x) for y,x in enumerate(PartitionJson) if x["TreeLink"]==k["Treelink"]][0]
                    PartitionJson[order]=InformPartitionJson(PartitionJson_k, k)
    return PartitionJson



class simulatorMol:
    def __init__(self, pathevolver='./evolver'):
        self.path=pathevolver
        self.EvolverOutputFile='mc.nex'
        self.Complexity=[]
        self.MI=[]
        self.Nomefile=""
        self.CurPartitioning=None
    def complexityEstimation(self,nomefile="mc.paml"):
        from math import log
        from utility import Table
        from Bio import AlignIO
        if nomefile.__class__=="".__class__:
            A=AlignIO.read(nomefile,"nexus")
        else:
            A=nomefile
        patterns=[A[:,x] for  x in range(len(A._records[0]))]
        F=Table(patterns).values()
        n=sum([x*log(x) for x in F if x!=0])
        N=sum(F)
        return n-N*log(N)
        

    def MakeDICTGapAndN(self,MSAref):
        """
        Find where the gap are
        """
        MissingChar="[?-NX]"
        misslist=[]
        #I assume that simulator use number from the tree and the number match the order of taxa in alignment
        for s in MSAref._records:
            points=[x.start() for x in list(re.finditer(MissingChar,s.seq.tostring()))]
            missdict.append(points)
        return misslist
    def AddGapAndN(self,MSA,LIST):
        """
        Add in simulated data the same gap and N than in the observed one
        """
        from Bio import Seq
        for s,m in zip(MSA._records,LIST):
            S=list(s.seq.tostring())
            for mm in m:
                S[mm]="-"
            S="".join(S)
            s.seq=Seq(S,alphabet=s.seq.alphabet)
        return MSA
            
    def MIEstimation(self,nomefile):
        from Bio import AlignIO
        from utility import Table
        alignobj=AlignIO.read(nomefile,"nexus")
        import itertools
        dna = ['A','T','C','G']
        dna=[x.lower() for x in dna]
        cases = [''.join(x) for x in itertools.product(dna, repeat=2)]
        alignlist=alignobj._records
        Pi=[]
        for seq in alignlist:
            tmp = Table(seq, cases=dna)
            l = sum(tmp.values())
            for x in tmp:
                tmp[x] = tmp[x] / float(l)
            Pi.append(tmp)
        L=len(alignlist)
        MutualInfo=[]
        names=[]
        for i in range(L):
            for j in range(i,L):
                MI=0
                sitelist=transpose([alignlist[i],alignlist[j]])
                sitelist=["".join(x) for x in sitelist]
                pattern=Table(sitelist, cases=cases) #levare pero' NA dai casi (quindi dalle chiavi do pattern)
                del pattern['NA']
                #print pattern
                l=float(sum(pattern.values()))
                for pat in pattern.keys():
                    bi,bj=pat
                    cpat=pattern[pat]/l
                    if cpat==0:
                        #print i,j, pat, cpat
                        continue
                    #print Pi[i][bi]
                    #print Pi[j][bj], pattern[pat]/l
                    #print (pattern[pat]/l)/((Pi[i][bi])*(Pi[j][bj]))
                    MI+=cpat*numpy.log((cpat)/((Pi[i][bi])*(Pi[j][bj])))
                    #print pattern[pat], Pi[i][bi], Pi[j][bj], l
                MutualInfo.append(MI)
                names.append((i+1,j+1))
        
        return MutualInfo, names

    def evolve(self,cmd='5\n0\n'):
        #esegue il programma di simulazione
        comfile=open('RR','w')
        comfile.write(cmd)
        comfile.close()
        os.popen(self.path+' < RR')
    def ReadingJson(self,Json, rep=1):
        import numpy
        PosteriorInfo=json.loads(Json)
        Posterior=PosteriorInfo["VariableParameters"]
        MSAspec=None
        if PosteriorInfo.has_key("FixedParameters"):
            MSAspec=PosteriorInfo["FixedParameters"]
        for p in Posterior:
            Model=p["model"]
            #store separately results of different partitions
            self.Complexity.append([])
            self.MI.append([])
            self.CurPartitioning=Model
            self.partitionOrder=Model.keys()
            for partition in self.partitionOrder:
                M=Model[partition]
                #inform json with general parameters if necessary
                if MSAspec:
                    M=InformPartitionJson(M,MSAspec[partition])
                M["replicates"]=str(rep)
                Param=GeneralFormat(M)
                #Add model specific part
                if M["type"].title()=="Protein":
                    #print ProteinFormat(M)
                    Param.update(ProteinFormat(M))
                    EvolverInput=InputAA.format(**Param)
                    self.Nomefile="MCAA.dat"
                    cmd='7\n0\n'
                else:
                    if M["matrix"]["size"]=="4X4":
                        Param.update(NucleotideFormat(M))
                        EvolverInput=InputBase.format(**Param)
                        self.Nomefile="MCbase.dat"
                        cmd='5\n0\n'
                    elif M["matrix"]["size"]=="64X64":
                        Param.update(CodonFormat(M))
                        EvolverInput=InputCodon.format(**Param)
                        self.Nomefile="MCcodon.dat"
                        cmd='6\n0\n'
                    elif M["matrix"]["size"]=="16X16":
                        Param.update(DubletFormat(M))
                        MysteryInput=InputM.format(**Param)
                        self.Nomefile="Mister"
                        cmd="Mistery"
                #write file and evolve it
                handle=open(self.Nomefile,"w")
                handle.write(EvolverInput)
                handle.close()
                self.evolve(cmd)
                #get scores
                self.Complexity[-1].append(self.complexityEstimation(self.EvolverOutputFile))
                #self.MI[-1].append(self.MIEstimation(self.EvolverOutputFile))
    def FinalScore(self, OriMSAfile, formatfile="nexus"):
        from Bio import AlignIO
        from Bio.Alphabet import DNAAlphabet
        oriMSA=AlignIO.read(OriMSAfile, formatfile)
        self.OriComplexity=[]
        for part in self.partitionOrder:
            r=self.CurPartitioning[part]['partitionRange']
            r=[y[:1]+y[1].split("\\") for y in [x.split("-") for x in r.split()]]
            sites=[]
            for rr in r:
                if len(rr)==2:
                    rr=rr+[1]
                elif len(rr)==1:
                    rr=rr+[rr[0]+1,1]
                start,end,step=map(int, rr)
                #minus one is to match python count with normal sites count
                sites+=range(start-1,end-1,step)
            MSAslices=[oriMSA[:,x:(x+1)] for x in range(len(oriMSA._records[0])) if x in sites]
            MSA=sum(MSAslices[1:],MSAslices[0])
            self.OriComplexity.append(self.complexityEstimation(MSA))
        self.Complexity=numpy.array(self.Complexity)
        self.OriComplexity=numpy.array(self.OriComplexity)
        L=float(len(self.Complexity))
        
        Pscore=sum(numpy.sum(self.Complexity,1)>sum(self.OriComplexity))/L
        Score=numpy.sum(self.Complexity,1)
        OriScore=sum(self.OriComplexity)
        output='<res>\n'
        output+='\t<P description="Bollback statistics" dataset="All">'+str(Pscore)+'</P>\n'
        output+='\t<meanE description="Mean Expected Value of MaxLikelihood" dataset="All">'+str(numpy.mean(Score))+'</meanE >\n'
        output+='\t<VarE description="Variance of MaxLikelihood" dataset="All">'+str(numpy.var(Score))+'</VarE >\n'
        output+='\t<MSqDev description="Mean Square Deviation Expected from Observed" dataset="All">'+str(numpy.mean((OriScore-Score)**2))+'</MSqDev >\n'
        output+='\t<Mobs description="Observed MaxLikelihood" dataset="All">'+str(OriScore)+'</Mobs>\n'
        output+='\t<Part description="List of Partitions in the dataset" dataset="All">'+",".join(self.partitionOrder)+'</Part>\n'
        Ls=(numpy.var(Score)+numpy.mean((OriScore-Score)**2))**0.5
        output+='\t<Ls description="Ibrahim statistics (square root of VarE+MSqDev)" dataset="All">'+str(Ls)+'</Ls>\n'
        output+='\t<ExpDist description="Expected distribution" dataset="All">'+",".join(map(str,Score))+'</ExpDist>\n'
        Pscores=numpy.sum(self.Complexity>self.OriComplexity,0)/L
        MeanScores=numpy.mean(self.Complexity,0)
        VarScores=numpy.var(self.Complexity,0)
        DevScores=numpy.mean((self.OriComplexity-self.Complexity)**2,0)
        if len(self.partitionOrder)>1:
            for pname,p,m,v,dev,obs,dist in zip(self.partitionOrder,Pscores,MeanScores,VarScores,DevScores,self.OriComplexity,list(self.Complexity.transpose())):
                output+='\t<P description="Bollback statistics" dataset="'+pname+'">'+str(p)+'</P>\n'
                output+='\t<meanE description="Mean Expected Value of MaxLikelihood" dataset="'+pname+'">'+str(m)+'</meanE >\n'
                output+='\t<VarE description="Variance of MaxLikelihood" dataset="'+pname+'">'+str(v)+'</VarE >\n'
                output+='\t<MSqDev description="Mean Square Deviation Expected from Observed" dataset="'+pname+'">'+str(dev)+'</MSqDev >\n'
                output+='\t<Mobs description="Observed MaxLikelihood" dataset="'+pname+'">'+str(obs)+'</Mobs>\n'
                Ls=(v+dev)**0.5
                output+='\t<Ls description="Ibrahim statistics (square root of VarE+MSqDev)" dataset="All">'+str(Ls)+'</Ls>\n'
                output+='\t<ExpDist description="Expected distribution" dataset="'+pname+'">'+",".join(map(str,dist))+'</ExpDist>\n'
        output+='</res>\n'
        return output
            
            
        
        

    

def findThinning(nexusfilename, burnin, Exsampling):
    """finding the """
    nexus=open(nexusfilename, 'r')
    nexusL=nexus.readlines()
    line=[l for l in nexusL if l.strip()[:5]=='mcmcp']
    if len(line)==0:
        line=[l for l in nexusL if l.strip()[:4]=='mcmc']
    line=line[0]
    line=[l.split('=') for l in line.split()[1:]]
    D={}
    D.update(line[:-1])
    ngen=int(D['ngen'])
    samplefreq=int(D['samplefreq']) 
    print ngen
    ngen=ngen/samplefreq
    print ngen
    ngen=ngen-int(burnin)
    thinning=ngen/int(Exsampling)
    print samplefreq,ngen, Exsampling,
    return  thinning

if __name__=="__main__":
    import os
    com={"-j":"prova.json"}
    count=1
    key=None
    for i in sys.argv:
        if key!=None:
            com[key]=i
            key=None
        if i[0]=="-":
            key=i
    spiegazione=""" 
    -j jsoninput
    -e path to simulator evolver
    -i input MSA
    -f input MSA format
    -r how many times each model need to be used for simulation
    """
    if len(com)<4:
        print spiegazione
    if not com.has_key("-e"):
        com["-e"]=os.path.dirname(os.path.realpath(__file__))+os.path.sep+"evolver"
    S=simulatorMol(pathevolver=com["-e"])
    handle=open(com["-j"],"r")
    JJstring=handle.read()
    handle.close()
    S.ReadingJson(JJstring)
    NexusInput=com["-i"]
    a=S.FinalScore(NexusInput,formatfile=com["-f"])
    sys.stdout.write(a)

