/**
 * Created by Administrator on 2015/9/20.
 */

import java.io.File;

/**
 * 获取指定目录下所有的文件,递归调用
 *
 * @author 咖啡
 *
 */
public class FileList {

    private static final String ROOT_DIR = "E:\\Temp";
    private static int count = 0;

    public static void main(String[] args) {

        Test test = new Test();
        String path = "G:\\Ghost-7xp8";

        find(new File(path));
        System.out.println("共有文件数: " + count);
    }

    /**
     * 是文件就输出,是目录就继续调用自己
     */
    public static void find(File file) {
        File[] fileList = file.listFiles();

        for (int i = 0; i < fileList.length; i++) {
            if (fileList[i].isDirectory()) {
                find(fileList[i]);
            } else {
                System.out.println(fileList[i]);
                count++;
            }
        }
    }










}
