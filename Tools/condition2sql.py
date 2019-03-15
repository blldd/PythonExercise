# -*- coding: utf-8 -*-
'''
    query_equal = {
        "event_id": event_id
    }
'''

def condition2sql(query_equal, query_like):

    condition_sql = " WHERE 1=1"

    # For equal.
    for key, value in query_equal.iteritems():

        if value is None or value.strip() == "":
            continue

        if isinstance(value, str) or isinstance(value, unicode):
            condition_sql += " and %s = '%s' " % (key, value)

        if isinstance(value, bool) or isinstance(value, int):
            condition_sql += " and %s = %s " % (key, value)

    # For like.
    for key, value in query_like.iteritems():
        if key is None or key.strip() == "" or value is None or value.strip() == "":
            continue
        condition_sql += " and %s like '%%%%%s%%%%' " % (key, value)

    return condition_sql
	
	
'''
	
	    Map<String, Object> queryLikeMap = new HashMap<String, Object>();
        queryLikeMap.put("doubtPro", doubtPro);
        queryLikeMap.put("goodsID", goodsID);
        queryLikeMap.put("goodsName", goodsName);
        queryLikeMap.put("goodsType", goodsType);
        queryLikeMap.put("predict", predict);
		
	    public String condition2sql(Map<String, Object> queryEqualMap,
                                Map<String, Object> queryLikeMap) {
        String condition_sql = " WHERE 1=1";
        // 相等查询
        for (Map.Entry<String, Object> entry: queryEqualMap.entrySet()){
            String field = entry.getKey();
            Object value = entry.getValue();

            if (field == null || field.trim().isEmpty()){
                continue;
            }

            if(value instanceof String){
                if (value.toString().trim().isEmpty()){
                    continue;
                }
                condition_sql += String.format(" and %s = '%s' ", field, value);
            }

            if(value instanceof Boolean || value instanceof Integer){
                condition_sql += String.format(" and %s = %s ", field, value.toString());
            }

        }

        // like 查询
        for (Map.Entry<String, Object> entry: queryLikeMap.entrySet()){
            String field = entry.getKey();
            String value = (String)entry.getValue();

            if (field == null || field.trim().isEmpty() || value == null || value.trim().isEmpty()){
                continue;
            }
            condition_sql += String.format(" and %s like '%%%s%%' ", field, value);

        }

        return condition_sql;
    }
'''