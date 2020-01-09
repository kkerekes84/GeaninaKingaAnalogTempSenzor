node {
   stage('init') {
      checkout scm
   }
   stage('build') {
      sh '''
         
        
         cp analog_temp.py analog_temp.py
  
         zip analog_temp.zip analog_temp.py
        
      '''
   }
   stage('deploy') {
      fileOperations([fileCopyOperation(excludes: '', flattenFiles: false, includes: '*.py', targetLocation: '/home/pi/Desktop/GeaninaKingaPipelineWithAzure')])
      azureWebAppPublish azureCredentialsId: env.AZURE_CRED_ID,
      resourceGroup: env.RES_GROUP, appName: env.WEB_APP, filePath: "**/analog_temp.zip"
   }
}
