/**
 * Created by Administrator on 2015/9/20.
 */

import java.io.File;

/**
 * ��ȡָ��Ŀ¼�����е��ļ�,�ݹ����
 *
 * @author ����
 *
 */
public class FileList {

    private static final String ROOT_DIR = "E:\\Temp";
    private static int count = 0;

    public static void main(String[] args) {

        Test test = new Test();
        String path = "G:\\Ghost-7xp8";

        find(new File(path));
        System.out.println("�����ļ���: " + count);
    }

    /**
     * ���ļ������,��Ŀ¼�ͼ��������Լ�
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
