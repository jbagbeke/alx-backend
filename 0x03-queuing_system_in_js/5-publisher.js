import redis from 'redis';


const publisher = redis.createClient({
    host: '127.0.0.1',
    port: 6379
}).on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log('Redis client not connected to the server:', error);
});

const channelName = 'holberton school channel';

function publishMessage(message, time) {
    setTimeout(() => {
        console.log('About to send', message);
        publisher.publish(channelName, message, (error, reply) => {
            if (error) {
                console.log(error);
            }
        });
    }, time);
}


publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
