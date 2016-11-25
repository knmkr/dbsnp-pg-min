#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
from decimal import Decimal, InvalidOperation

def mustache(x):
    return '{' + ','.join(x) + '}'

for line in sys.stdin:
    # .frq (basic allele frequency report)
    # Produced by --freq. Valid input for --read-freq.
    #
    # A text file with a header line, and then one line per variant with the following six fields:
    #
    #   CHR      Chromosome code
    #   SNP      Variant identifier
    #   A1       Allele 1 (usually minor)
    #   A2       Allele 2 (usually major)
    #   MAF      Allele 1 frequency
    #   NCHROBS  Number of allele observations

    # E.g.
    #
    # [.frq]
    # CHR     SNP   A1   A2          MAF  NCHROBS
    # 12   rs671    A    G      0.03591     4984

    # .frqx (genotype count report)
    # Produced by --freqx. Valid input for --read-freq.
    #
    # A text file with a header line, and then one line per variant with the following ten fields:
    #
    #   CHR         Chromosome code
    #   SNP         Variant identifier
    #   A1          Allele 1 (usually minor)
    #   A2          Allele 2 (usually major)
    #   C(HOM A1)   A1 homozygote count
    #   C(HET)      Heterozygote count
    #   C(HOM A2)   A2 homozygote count
    #   C(HAP A1)   Haploid A1 count (includes male X chromosome)
    #   C(HAP A2)   Haploid A2 count
    #   C(MISSING)  Missing genotype count

    # E.g.
    #
    # [.frqx]
    # CHR	SNP	A1	A2	C(HOM A1)	C(HET)	C(HOM A2)	C(HAP A1)	C(HAP A2)	C(MISSING)
    # 12	rs671	A	G	20	139	2333	0	0	0

    if line.lstrip().startswith('CHR'):
        continue

    frq_rows, chrom_frqx, snp_frqx, a1_frqx, a2_frqx, n_a1_hom, n_het, n_a2_hom, n_a1_hap, n_a2_hap, n_missing = [x for x in line.rstrip().split('\t') if x != '']
    chrom, snp, a1, a2, a1_af, nchrobs = [x for x in frq_rows.split(' ') if x != '']

    try:
        assert chrom == chrom_frqx
        assert snp == snp_frqx
        assert a1 == a1_frqx
        assert a2 == a2_frqx
    except AssertionError as e:
        print >>sys.stderr, '[ERROR] Invalid .frq/.frqx line', line
        continue

    try:
        a2_af = '{}'.format(Decimal(1) - Decimal(a1_af))
    except InvalidOperation:
        print >>sys.stderr, '[ERROR] Invalid .frq/.frqx line', line
        continue

    # [.csv]
    # 671	{A,G}	{0.03591,0.96409}	{20,139,2333,0,0,0}
    print '\t'.join([snp,
                     mustache([a1, a2]),
                     mustache([a1_af, a2_af]),
                     mustache([n_a1_hom, n_het, n_a2_hom, n_a1_hap, n_a2_hap, n_missing])])
