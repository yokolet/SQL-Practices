SELECT count(e.customer_organization_id) AS subordinates_count, o.id
FROM organizations AS o
FULL JOIN enterprise_sales_enterprise_customers AS e
ON o.id = e.sales_organization_id
GROUP BY o.id
ORDER BY o.id;
