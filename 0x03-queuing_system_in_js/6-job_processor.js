import { push_notification_code } from './6-job_creator.js'


function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}


push_notification_code.process('Push_Notification', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
})
