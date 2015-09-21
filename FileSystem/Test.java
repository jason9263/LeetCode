/**
 * Created by Administrator on 2015/9/20.
 */


import java.io.*;
import java.util.*;

public class Test {

    public static void main(String args[]) {
        Test test = new Test();
        String path = "G:\\Program Files (x86)\\VMware\\VMware Workstation";
        String rpath = "G:\\b.txt";
        try {

            List<FileInfo> FL = test.getFilesByPath(path);

            test.write(FL, rpath);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    private static void write(List<FileInfo> FL, String rpath) throws IOException {
        File file = new File(rpath);//
        if (!file.exists()) {//
            file.createNewFile();
        }
        //
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(file));
        // Write the Information
        String temps = "";
        long tempsize = 0;
        FileInfo tempfi = new FileInfo();
        for (int i = 0; i < FL.size(); i++) {
            tempfi = FL.get(i);

            temps = tempfi.PrintAtt(tempfi);
            bufferedWriter.write(temps);

            bufferedWriter.newLine();//
            bufferedWriter.flush();//
        }

        bufferedWriter.close();//
    }


    public List<FileInfo> getFilesByPath(String path) throws Exception {

        //
        String encoding = System.getProperty("file.encoding");
        List<FileInfo> fileList = new ArrayList<FileInfo>();
        try {
            //
            File file = new File(new String(path.getBytes("UTF-8"), encoding));

            //
            if (file.exists() && file.isDirectory() && file.canRead()) {
                /**
                 *
                 */
                File[] files = file.listFiles(new FileFilter() {
                    @Override
                    public boolean accept(File f) {
                        return !f.isHidden();
                    }
                });
                /**
                 * java
                 */
                String temps = "";

                String extendstr = "";

                Set<String> extendset = new HashSet<>();

                for (File f : files) {
                    FileInfo fileInfo = new FileInfo();
                    //
                    temps = new String(f.getName().getBytes(encoding), "UTF-8");
                    //System.out.println(temps);

                    extendstr = f.getName().substring(f.getName().lastIndexOf(".") + 1, f.getName().length());
                    System.out.println(extendstr);
                    extendset.add(extendstr);

                    fileInfo.setName(temps);
                    fileInfo.setSize(f.length());
                    fileInfo.setLastModified(new Date(f.lastModified()));
                    fileInfo.setDir(f.isDirectory());
                    fileInfo.setHid(f.isHidden());
                    fileInfo.setRead(f.canRead());
                    fileInfo.setwritten(f.canWrite());
                    fileInfo.setexcute(f.canExecute());


                    fileList.add(fileInfo);
                }

                System.out.println(extendset.size());

                
            } else {
                throw new Exception("Paht:" + path + ", exists:" + file.exists() + ", canRead:" + file.isDirectory());
            }
        } catch (UnsupportedEncodingException e1) {
            e1.printStackTrace();
        }



        return fileList;

    }

}
