BEGIN;
SELECT * FROM plan(2);

SELECT set_eq(
  'SELECT snp_id,snp_current,allele,freq::text FROM get_tbl_allele_freq_by_rs_history(ARRAY[671, 2230021, 4134524, 4986830, 60823674])',
  $$ VALUES
  (671,      671, '{G,A}'::varchar[], '{0.7995,0.2005}'),
  (2230021,  671, '{G,A}'::varchar[], '{0.7995,0.2005}'),
  (4134524,  671, '{G,A}'::varchar[], '{0.7995,0.2005}'),
  (4986830,  671, '{G,A}'::varchar[], '{0.7995,0.2005}'),
  (60823674, 671, '{G,A}'::varchar[], '{0.7995,0.2005}')
  $$
);

SELECT set_eq(
  'SELECT snp_id,snp_current,allele,freq::text FROM get_tbl_allele_freq_by_rs_history_1000genomes_phase1(ARRAY[671])',
  $$ VALUES
  (671,      671, '{G,A}'::varchar[], '{0.7832,0.2168}')
  $$
);

SELECT * FROM finish();
ROLLBACK;
