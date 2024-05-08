import kue from 'kue';


const push_notification_code_2 = kue.createQueue();




const blackListedNumbers = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0);
    if (blackListedNumbers.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

push_notification_code_2.process('Push_Notification', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});