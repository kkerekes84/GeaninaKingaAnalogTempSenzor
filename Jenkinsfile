node {
   stage('init') {
      checkout scm
      fileOperations([fileCopyOperation(excludes: '', flattenFiles: false, includes: '*.py', targetLocation: '/home/pi/Desktop/GeaninaKingaPipelineWithAzure')])
   }
   
   stage('test') {
      sh 'python /home/pi/Desktop/GeaninaKingaPipelineWithAzure/test.py'
   }
   stage('build') {
      sh '''
  
         zip analog_temp.zip analog_temp.py
         zip analog_temp_mqtt.zip analog_temp_senzor_mqtt.py
        
      '''
   }
   stage('deploy') {
      
      azureWebAppPublish azureCredentialsId: env.AZURE_CRED_ID,
      resourceGroup: env.RES_GROUP, appName: env.WEB_APP, filePath: "**/analog_temp.zip"
      
   }
}
