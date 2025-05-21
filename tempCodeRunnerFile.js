use('ecommerce');
db.getCollection('produtos').find({ preco: { $gt: 100 } });