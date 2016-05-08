SET default_parallel 4;
rows = LOAD '/pig/stackoverflow_users.xml' USING org.apache.pig.piggybank.storage.XMLLoader('row') as data:chararray;
users = FOREACH rows GENERATE REGEX_EXTRACT(data,'<row Id="(.*?)"(.*)',1) as id:chararray, data as row:chararray;
ids = LOAD '/sample-output2/android/' USING PigStorage(',') AS (id:chararray);
result = JOIN ids by id, users by id;
result1 = FOREACH result GENERATE users::row as row;
STORE result1 INTO '/pig_output';
-- USING JsonStorage();
