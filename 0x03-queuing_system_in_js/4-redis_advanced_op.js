import redis from 'redis';


const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379
}).on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log('Redis client not connected to the server: ', error);
});


client.hset('HolbertonSchools', 'Portland', '50', (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hset('HolbertonSchools', 'Seattle', '80', (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hset('HolbertonSchools', 'New York', '20', (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hset('HolbertonSchools', 'Bogota', 20, (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hset('HolbertonSchools', 'Cali', 40, (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hset('HolbertonSchools', 'Paris', 2, (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        redis.print(null, reply);
    }
});

client.hgetall('HolbertonSchools', (error, reply) => {
    if (error) {
        console.log(error);
    } else {
        console.log(reply)
    }
})
