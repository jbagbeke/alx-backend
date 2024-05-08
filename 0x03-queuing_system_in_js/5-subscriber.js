import redis from 'redis';


const client = redis.createClient({
    host: '127.0.0.1',
    port: 6379
}).on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (error) => {
    console.log('Redis client not connected to the server:', error);
});

const channelName = 'holberton school channel';

client.subscribe(channelName);

client.on('message', (channel, message) => {
    if (channel === channelName) {
        if (message === 'KILL_SERVER') {
            client.unsubscribe(channelName);
            client.quit();
        }
        console.log(message);
    }
});
