#!/usr/bin/env nextflow

/*
 * PDB sources -> respective hemes' mol2 (3d coords)
 * https://www.nextflow.io/docs/latest/process.html
 * Ctrl+F to "proteins" to see filename syntax
 *
 * Further, $baseDir = do not use, deprecated
 * $projectDir = where this nextflow script is located
 */

print "ROHAN RIDES TO GONDOR'S AID!"

pdb_files = Channel.fromPath('~/project/pdb_src/*.pdb' )
hemePrepScript = "$projectDir/heme_prep.py"

process hemePrep {
   input:
   path pdb_files

    "echo 'cats'"
    /*
    path currentPDB from pdb_files
    
    "chimera --nogui $hemePrepScript pdb_src/1w0e.pdb"
*/
}
workflow{
    hemePrep
}

workflow.onComplete { 
	log.info ( workflow.success ? "Done!" : "Oops .. something went wrong" )
}