# hem_docking

(Current as of 6 June 2022. This readme hopefully gives a good idea of what I intend to do, as well as inform my future self about the intended scope and direction of the project.)

Assessing the distribution of binding affinities/energies of HEM in hemoprotein pockets. Follow up to thesis work. This is a provisional description and citations/descriptions of methodology will be provided or updated as the work progresses!

The results of my thesis work (available here: https://github.com/patimus-prime/heme-binding) demonstrated the binding pockets of heme are mostly, but not completely, nonpolar; polar residues are still present, required to coordinate with the iron atom and propionate residues of heme.

The binding pockets of hemoproteins host both heme, a cofactor, and the ligands of each protein. Hemoproteins are diverse and the pockets vary by their host protein's folds, and the residues required to bind the ligand(s).
The variety and distribution of structural features have been reported in other works, but a distribution of predicted binding affinities/energies, related to those structural features, has not yet been reported. (1,2,3)

What I intend to do here is to relate structural features to those predicted energies; both by clustering by features (e.g. % nonpolar residues) and estimation of energies by features (using a variety of machine learning regression algorithms), as well as maybe from just the sequence (a stretch -- likely only even fantasized after importing a considerable number of PDBs, generating a lot of data).

This work will hopefully be of some use to protein engineering efforts; either by identification of structures with POWERFUL binding affinity of heme (maybe translating to improved enzymatic efficiency) or by establishing some baseline from which to compare results of residue mutations/cofactor substitutions. (publications I hope to find some example utility in are below, 4-6).

Those mutations/substitutons may also to some degree be part of this work -- attempting to reproduce wet lab results or modeling, retroactively predicting those results via computation.

# Methods

Very provisional description of methods; skeleton pipeline is thus far built out, but score functions, methods of calculating free energy, degree of involvement of sequence comparison TBD:

Most/all work will be run using AWS; this will hopefully spare my laptop from death by melting. So far (6 June 2022) I'm using one t3.2xlarge instance, running Ubuntu 20.04 and Pyrosetta 4, release 319, Python 3.9; may evolve to use more instances e.g. auto-scale groups/AWS Batch. 

This is a personal project... so uh, costs will very much be in mind and certainly reported at the end, along with whatever resources/network architecture are used. If generation of results is slow, I may use randomly generated data to train downstream models in the meantime. Just to have everything built out.

Initially, generated scores/predicted energy will be related to structural features generated from my thesis work; alternatively, new volumes/surface areas will be calculated using 


# Citations

Citing within this readme below:

1. Li, Ting, Herbert L. Bonkovsky, and Jun-tao Guo. "Structural analysis of heme proteins: implications for design and prediction." BMC structural biology 11.1 (2011): 1-13.
2. Schneider, Sabine, et al. "Diversity and conservation of interactions for binding heme in b-type heme proteins." Natural product reports 24.3 (2007): 621-630.
3. Liong, Elaine C., et al. "Waterproofing the heme pocket: role of proximal amino acid side chains in preventing hemin loss from myoglobin." Journal of Biological Chemistry 276.12 (2001): 9093-9100.
4. Reeder, Brandon J., et al. "Tyrosine residues as redox cofactors in human hemoglobin: implications for engineering nontoxic blood substitutes." Journal of Biological Chemistry 283.45 (2008): 30780-30787.
5. Coelho, Pedro S., et al. "A serine-substituted P450 catalyzes highly efficient carbene transfer to olefins in vivo." Nature chemical biology 9.8 (2013): 485-487.
6. Natoli, Sean N., and John F. Hartwig. "Noble− metal substitution in hemoproteins: an emerging strategy for abiological catalysis." Accounts of chemical research 52.2 (2019): 326-335.
7. Key, Hanna M., et al. "Beyond iron: iridium-containing P450 enzymes for selective cyclopropanations of structurally diverse alkenes." ACS central science 3.4 (2017): 302-308.
