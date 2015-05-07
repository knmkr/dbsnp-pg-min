# dbsnp-pg-min

Minimal PostgreSQL schemas & functions for Human data in [NCBI dbSNP](http://www.ncbi.nlm.nih.gov/SNP/).

- NCBI dbSNP (a public archive for genetic variation) is distributed in MS SQL Server schema.
- We simply port minimal original MS SQL Server schema to PostgreSQL,
- and implemented query functions to get [SNP information like in dbSNP web CGI](http://www.ncbi.nlm.nih.gov/projects/SNP/snp_ref.cgi?rs=671) in command line interface.


## Getting Started

    $ createdb --owner=username dbsnp_b141           # 0. Create new PostgreSQL database for dbSNP
    $ ./01_fetch_dbsnp.sh                            # 1. Fetch dbSNP data from dbSNP FTP site
    $ ./02_drop_create_table.sh dbsnp_b141 username  # 2. Create PostgreSQL tables for dbSNP
    $ ./03_import_dbsnp.sh      dbsnp_b141 username  # 3. Import dbSNP data into PostgreSQL tables
    $ ./04_add_constraints.sh   dbsnp_b141 username  # 4. Add constraints (index, etc.) to tables


## Usage example

### Get chromosome and position for given rs\#

```
SELECT
    snp_id, chr, pos
FROM
    b141_snpchrposonref
WHERE
    snp_id = 333333;
--  snp_id | chr |    pos
-- --------+-----+-----------
--  333333 | 3   | 124609540
-- (1 row)
```

or simply

```
SELECT get_pos_by_rs(333333);
-- (3,124609540)
```

### Get current rs\# for given rs\#

```
SELECT
   rshigh, rscurrent
FROM
   rsmergearch
WHERE rshigh = ANY(ARRAY[330, 331, 332]);
--  rshigh | rscurrent
-- --------+-----------
--     332 | 121909001
-- (1 row)

```
SELECT get_current_rs(332);
-- 121909001
```


## Unit Tests

To run tests:

```
$ cd test
$ ./test.sh
```

Requirements:
  - PostgreSQL extension: [pgTAP (a unit testing framework for PostgreSQL)](http://pgtap.org/)
  - [pg_prove (a command-line tool for running and harnessing pgTAP tests)](http://search.cpan.org/dist/TAP-Parser-SourceHandler-pgTAP/)


## Notes

- Only human [9606] data is supported.
- Build versions of dbSNP and human reference genome assembly are:

| database name             | dbSNP    | reference genome |
|---------------------------|----------|------------------|
| human_9606                | (latest) | (latest)         |
| human_9606_b142_GRCh38    | b142     | GRCh38           |
| human_9606_b142_GRCh37p13 | b142     | GRCh37p13        |
| human_9606_b141_GRCh38    | b141     | GRCh38           |
| human_9606_b141_GRCh37p13 | b141     | GRCh37p13        |


## Lisence

See LISENCE


## Author

@knmkr
