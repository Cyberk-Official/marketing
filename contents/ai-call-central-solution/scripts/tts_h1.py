import asyncio
import os
import edge_tts

# H1 Script — Audio only (spoken words extracted from script)
sentences = [
    # Scene 1: Hook (00:00 → 00:33)
    "Thiết kế hệ thống tổng đài Ây Ai — tự động gọi điện và chốt lịch hẹn khi có lead mới.",
    "Luồng cơ bản thế này: người dùng điền form trên landing page, hệ thống bắn data về, trigger cuộc gọi Ây Ai trong chưa đầy một phút. Ây Ai xác nhận nhu cầu, chốt lịch hẹn, hoàn toàn tự động.",
    "Nghe đơn giản, nhưng có ba bài toán cần giải trước: làm sao Ây Ai hiểu đúng bài toán kinh doanh, tuân thủ pháp luật Singapore, và phản hồi đủ nhanh để người gọi không cúp máy. Tôi đi lần lượt.",

    # Scene 2A: Yêu cầu bài toán (00:33 → 00:50)
    "Bài toán thực tế: một startup vận hành mô hình đặt lịch hẹn. Yêu cầu dự án gồm 5 điểm — gọi lại ngay khi có lead, xác nhận nhu cầu trên cuộc gọi, chốt lịch hẹn với chuyên viên, tự gọi lại nếu không nghe máy, và chuyển sang người thật khi cần.",

    # Scene 2B: Startup context (00:50 → 01:05)
    "Điểm quan trọng: đây là startup giai đoạn đầu, gần như chưa có người dùng thực tế. Thông tin này đòi hỏi hệ thống phải tiết kiệm tối đa chi phí khi chưa có người dùng — nếu phải trả hàng trăm đô mỗi tháng cho server thì lãng phí. Nhưng khi startup thành công và lượng cuộc gọi tăng đột biến, hệ thống phải tự động đáp ứng được — chỉ cần trả thêm tiền theo lượng sử dụng là xong.",

    # Scene 2C: 3 ràng buộc (01:05 → 01:45)
    "Từ bối cảnh đó, tôi xác định 3 ràng buộc. Thứ nhất — trí tuệ hội thoại. Ây Ai phải hiểu bài toán kinh doanh, mỗi ngành hỏi khác nhau, phân loại nhu cầu rồi chốt lịch hẹn ngay — và kịch bản phải dễ thay đổi mà không cần viết lại code. Thứ hai — tuân thủ pháp luật. Singapore có 3 lớp luật chồng nhau, Ây Ai chỉ được hỏi và book, không được tư vấn sản phẩm.",
    "Thứ ba — tốc độ phản hồi. Khi người gọi nói xong một câu, Ây Ai phải trả lời ngay. Đợi 2 đến 3 giây mỗi lần thì người ta cúp máy. Hệ thống phải phản hồi dưới 1 giây, dù đang xử lý thông tin phức tạp phía sau. Tôi đi vào cách giải từng bài.",

    # Scene 3A: Luận điểm 1 — Serverless + Neon (01:45 → 03:00)
    "Vì đây là startup giai đoạn đầu, tôi chọn toàn bộ hạ tầng theo nguyên tắc: không có cuộc gọi nào thì không mất đồng nào. Thay vì thuê server chạy 24 trên 7, tôi dùng serverless — hệ thống chỉ thức khi có việc, xong lại ngủ.",
    "Database cũng vậy — dùng Neon, một loại database tự động tắt khi không ai truy cập, tự bật lại trong vài trăm mili-giây khi cần. Tháng đầu chưa có cuộc gọi nào? Chi phí hạ tầng gần bằng 0. Tháng sau có 1000 cuộc gọi? Chỉ trả tiền cho đúng 1000 cuộc đó.",
    "Về phần voice — thay vì tự xây dựng toàn bộ engine giọng nói, tôi dùng nền tảng managed sẵn có. Nền tảng này xử lý toàn bộ việc nghe, hiểu, trả lời, và gọi điện. Tôi chỉ cần tập trung vào nội dung cuộc hội thoại và logic kinh doanh. Chi phí cuối cùng: khoảng 0 chấm 11 đô một phút, bao gồm tất cả.",

    # Scene 3B: Luận điểm 2 — Kịch bản thông minh (03:00 → 04:05)
    "Thay vì viết một đoạn chỉ dẫn dài rồi hy vọng Ây Ai tự biết phải làm gì, tôi thiết kế cuộc gọi như một luồng có nhiều bước rõ ràng — mỗi bước Ây Ai chỉ tập trung vào đúng một việc. Bước chào hỏi thì chào hỏi, bước hỏi nhu cầu thì hỏi nhu cầu, bước chốt lịch thì chốt lịch.",
    "Ây Ai không cần nhớ toàn bộ kịch bản — chỉ cần xử lý đúng bước hiện tại. Nên Ây Ai trả lời chính xác hơn, nhanh hơn — mỗi lượt dưới 2 câu, cuộc trò chuyện tự nhiên, không có khoảng im lặng. Và khi cần thay đổi kịch bản — thêm câu hỏi, đổi thứ tự, điều chỉnh cho từng ngành — chỉ cần sửa đúng bước đó, không ảnh hưởng phần còn lại.",
    "Thêm một lớp nữa: trong lúc Ây Ai đang xử lý việc phức tạp như kiểm tra lịch trống, Ây Ai vẫn nói với người gọi 'Tôi đang kiểm tra, một chút nhé' — không bao giờ để im lặng. Người gọi luôn cảm thấy được phản hồi.",

    # Scene 3C: Luận điểm 3 — Chốt lịch + Compliance (04:05 → 05:36)
    "Khi Ây Ai gọi nhiều người cùng lúc, hai cuộc gọi có thể cùng chốt một khung giờ trong cùng một giây. Giải pháp: mỗi lịch hẹn được đánh một mã duy nhất. Nếu hai cuộc gọi cùng chốt, hệ thống chỉ chấp nhận cái đầu tiên, cái còn lại tự động đề xuất khung giờ khác. Người gọi không hề biết có xung đột.",
    "Quy trình bắt buộc: Ây Ai xác nhận nhu cầu xong mới đề xuất lịch. Đưa ra 2 đến 3 khung giờ, người gọi xác nhận bằng giọng nói, rồi mới chốt. Không bao giờ book trước khi qualify. Dữ liệu lịch hẹn nằm trên Neon database — cùng hạ tầng serverless, cùng nguyên tắc trả tiền theo lượng dùng.",
    "Về tuân thủ pháp luật Singapore: thay vì dựa vào việc Ây Ai nhớ danh sách những gì không được nói — cách này không đáng tin — tôi thiết kế luồng hội thoại sao cho Ây Ai không có cơ hội vi phạm. Ai đó hỏi 'bảo hiểm nào tốt nhất?' — hệ thống tự động chuyển sang người thật. Quyết định này được gắn cứng vào kiến trúc, không phải do Ây Ai tự phán đoán.",
    "Sau mỗi cuộc gọi, hệ thống tự kiểm tra xem Ây Ai có vô tình đưa ra lời tư vấn nào không. Và khi gọi mà không ai nghe — hệ thống tự động gọi lại 2 đến 3 lần, cách nhau vài giờ, chỉ trong khung giờ cho phép. Nếu vẫn không nghe, đánh dấu và dừng — không spam.",

    # Scene 4: Stick (05:36 → 06:18)
    "Quay lại sơ đồ tổng quan. Chi phí hạ tầng khi chưa có cuộc gọi: gần bằng 0. Chi phí khi vận hành: khoảng 0 chấm 11 đô một phút, bao gồm tất cả. Callback dưới 60 giây. 100% không trùng lịch hẹn. Tuân thủ pháp luật được đảm bảo bằng kiến trúc chứ không phải bằng hy vọng.",
    "Tổng đài Ây Ai cho startup không cần phức tạp — cần đúng thiết kế: hạ tầng không tốn tiền khi chưa dùng, kịch bản hội thoại dễ thay đổi, và tuân thủ pháp luật gắn cứng vào kiến trúc. Tập tiếp theo: thiết kế Ây Ai song ngữ Anh-Hoa — khi không engine nhận diện giọng nói nào hiểu Singlish.",

    # Scene 5: CTA (06:18 → 07:00)
    "Là một nhà điều hành doanh nghiệp — dù trong bất động sản, bảo hiểm, hay dịch vụ tư vấn — nếu bạn đang tìm giải pháp tự động hóa tổng đài và chốt lịch hẹn, hãy liên hệ CyberK để cùng thảo luận.",
    "Nếu bạn muốn nghe nhiều hơn về thiết kế hệ thống Ây Ai, hãy like, comment và share nhé.",
]

OUTPUT_FILE = "/Users/anderson/Desktop/works/marketing/contents/ai-call-central-solution/videos/01_h1_voiceover.mp3"

async def synthesize_sentence(idx, sentence, temp_files):
    temp_file = f"temp_h1_s{idx}.mp3"
    retries = 3
    for attempt in range(retries):
        try:
            print(f"Synthesizing sentence {idx+1}/{len(sentences)} (attempt {attempt+1})...")
            communicate = edge_tts.Communicate(sentence, "vi-VN-NamMinhNeural")
            await communicate.save(temp_file)
            temp_files.append(temp_file)
            print(f"  ✅ Sentence {idx+1} completed.")
            return True
        except Exception as e:
            print(f"  ❌ Error on sentence {idx+1}: {e}. Retrying in 2s...")
            await asyncio.sleep(2)
    print(f"  ❌ Failed sentence {idx+1} after {retries} attempts.")
    return False

async def amain():
    temp_files = []
    success = True
    for idx, sentence in enumerate(sentences):
        res = await synthesize_sentence(idx, sentence, temp_files)
        if not res:
            success = False
            break

    if success:
        print(f"\nConcatenating {len(temp_files)} MP3 files...")
        with open(OUTPUT_FILE, "wb") as outfile:
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    with open(temp_file, "rb") as infile:
                        outfile.write(infile.read())
        print(f"✅ Generated: {OUTPUT_FILE}")

    print("Cleaning up temp files...")
    for temp_file in temp_files:
        if os.path.exists(temp_file):
            try:
                os.remove(temp_file)
            except Exception as e:
                print(f"Error deleting {temp_file}: {e}")

if __name__ == "__main__":
    asyncio.run(amain())
