from pathlib import Path
import html
import json

ROOT = Path('/Volumes/Data/Project/GitGam')
REPORT = Path('/Volumes/Data/Project/GAM-Tool/reports/product-brochures-20261110')
PRODUCTS = []

def add(repo, name, icon, color, sources, vi, en):
    PRODUCTS.append(dict(repo=repo, name=name, icon=icon, color=color,
                         sources=sources, vi=vi, en=en))

# Each locale: category, headline, introduction, audience, four features,
# three getting-started steps, three business applications, scope note.
add('Account', 'GitGam Account', 'key', 'teal',
    ['README.md', 'docs/account-ownership.md', 'docs/account-billing.md', 'web/src/pages/Account'],
    ['Tài khoản & tổ chức', 'Một tài khoản.\nKết nối cả đội ngũ.',
     'Công việc thuận hơn khi mỗi người có một điểm bắt đầu rõ ràng. GitGam Account giúp doanh nghiệp quản lý tài khoản, công ty và quyền truy cập các ứng dụng GitGam trong cùng một nơi.',
     'Doanh nghiệp nhiều bộ phận, đội nhóm cộng tác và quản trị viên hệ thống.',
     [('Đăng nhập tập trung', 'Dùng tài khoản GitGam để truy cập các ứng dụng đã được cấp quyền.'), ('Đúng công ty, đúng công việc', 'Chọn tổ chức cần làm việc và giữ rõ không gian của từng công ty.'), ('Hồ sơ dễ quản lý', 'Cập nhật thông tin cá nhân và theo dõi các tổ chức liên quan.'), ('Truy cập có kiểm soát', 'Quản lý thành viên và quyền vào ứng dụng theo nhu cầu của doanh nghiệp.')],
     [('Chuẩn bị tổ chức', 'Người quản trị thiết lập công ty và ứng dụng cần dùng.'), ('Kết nối thành viên', 'Thêm đội ngũ và cấp quyền truy cập phù hợp.'), ('Bắt đầu cộng tác', 'Mỗi người mở ứng dụng, đăng nhập và chọn công ty được phép.')],
     [('Đội nhóm mới', 'Tạo điểm khởi đầu chung khi đưa GitGam vào công việc.'), ('Doanh nghiệp nhiều công ty', 'Chuyển không gian làm việc theo tổ chức được cấp quyền.'), ('Quản trị tập trung', 'Theo dõi ai có thể sử dụng ứng dụng nào.')],
     'Quyền vào ứng dụng và quyền xử lý nghiệp vụ được quản lý riêng; thành viên chỉ thấy và làm những việc được cấp phép.'],
    ['Identity & organizations', 'One account.\nA connected team.',
     'Work feels simpler when everyone has a clear place to begin. GitGam Account brings accounts, companies and access to GitGam applications together for your business.',
     'Businesses with several departments, collaborative teams and system administrators.',
     [('A shared sign-in', 'Use your GitGam account to enter applications your organization has enabled for you.'), ('The right company', 'Choose where to work while keeping each company’s workspace distinct.'), ('Profiles in one place', 'Maintain personal details and see the organizations connected to your account.'), ('Access with purpose', 'Manage members and application access around your business needs.')],
     [('Prepare your organization', 'An administrator sets up the company and applications.'), ('Bring people in', 'Add the team and assign the access each person needs.'), ('Start working together', 'Open an application, sign in and choose an authorized company.')],
     [('New teams', 'Give everyone a shared starting point for adopting GitGam.'), ('Several companies', 'Move between organizations you are authorized to access.'), ('Central administration', 'Keep a clearer view of who can use each application.')],
     'Application admission and business permissions are managed separately. Members work within the access assigned to them.'])

add('Accounting', 'GitGam Accounting', 'chart', 'teal',
    ['README.md', 'web/src/pages', 'docs/accounting-integrations.md'],
    ['Kế toán & tài chính', 'Sổ sách rõ ràng.\nQuyết định vững vàng.',
     'Từ chứng từ hằng ngày đến báo cáo cuối kỳ, GitGam Accounting giúp đội kế toán theo dõi công việc có trình tự, để người quản lý hiểu hơn bức tranh tài chính của doanh nghiệp.',
     'Phòng kế toán, doanh nghiệp nhiều chi nhánh và đội ngũ quản lý tài chính.',
     [('Chứng từ có quy trình', 'Lập, gửi duyệt và ghi sổ; theo dõi điều chỉnh khi cần.'), ('Thu chi & công nợ', 'Quản lý tiền mặt, ngân hàng, đối tượng và các khoản phải thu, phải trả.'), ('Báo cáo dễ theo dõi', 'Xem nhật ký, sổ cái, cân đối và các báo cáo từ số liệu đã ghi sổ.'), ('Kiểm soát cuối kỳ', 'Đối chiếu, khóa kỳ, lưu bản báo cáo và xem lịch sử thay đổi.')],
     [('Thiết lập nền tảng', 'Chuẩn bị kỳ kế toán, danh mục và quyền theo chi nhánh.'), ('Ghi nhận hằng ngày', 'Nhập chứng từ, kiểm tra, phê duyệt rồi ghi sổ.'), ('Đối chiếu & nhìn lại', 'Rà công nợ, kiểm tra chênh lệch và lập báo cáo theo kỳ.')],
     [('Kế toán nội bộ', 'Gom nghiệp vụ về một quy trình dễ theo dõi.'), ('Quản lý chi nhánh', 'Phân công người xử lý theo phạm vi phù hợp.'), ('Lãnh đạo doanh nghiệp', 'Trao đổi kế hoạch dựa trên số liệu đã ghi nhận.')],
     'Nhận hóa đơn tự động qua email và đọc hóa đơn bằng OCR chưa được kết nối. Số liệu, chính sách thuế và báo cáo cần được đội kế toán kiểm tra trước khi sử dụng.'],
    ['Accounting & finance', 'Clearer books.\nMore grounded decisions.',
     'From everyday vouchers to period-end reports, GitGam Accounting gives finance teams a structured way to work and helps business leaders understand the financial picture.',
     'Accounting departments, businesses with branches and finance management teams.',
     [('A voucher workflow', 'Prepare, submit, approve and post vouchers, with adjustments when needed.'), ('Cash & balances', 'Manage cash, bank activity, partners, receivables and payables.'), ('Reports with context', 'Review journals, ledgers, balances and reports built from posted entries.'), ('A clearer period close', 'Reconcile, close periods, save report snapshots and review change history.')],
     [('Set the foundation', 'Prepare accounting periods, catalogs and branch permissions.'), ('Record daily activity', 'Enter vouchers, review them, obtain approval and post.'), ('Reconcile & reflect', 'Check balances, review differences and prepare period reports.')],
     [('Internal accounting', 'Bring everyday finance work into a traceable process.'), ('Branch management', 'Assign work within the appropriate branch scope.'), ('Business leadership', 'Discuss plans using recorded financial information.')],
     'Automated invoice email intake and OCR are not connected. Your accounting team should review figures, tax policies and reports before relying on them.'])

add('Building', 'GitGam Building', 'building', 'blue',
    ['README.md', 'web/src/building/catalog.js', 'docs/technical-register.md', 'docs/meter-qr.md'],
    ['Quản lý tòa nhà', 'Chăm chút vận hành.\nAn tâm mỗi ngày.',
     'GitGam Building giúp ban quản lý gom hồ sơ, chỉ số và công việc vận hành về cùng một nơi, để phối hợp chăm sóc tòa nhà có tổ chức hơn.',
     'Ban quản lý tòa nhà, đơn vị vận hành và doanh nghiệp quản lý nhiều bất động sản.',
     [('Hồ sơ tập trung', 'Theo dõi cấu trúc bất động sản, căn hộ và các hồ sơ liên quan.'), ('Chỉ số & kỳ phí', 'Ghi chỉ số đồng hồ, lập kỳ phí và theo dõi khoản phải thu.'), ('Thu tiền rõ ràng', 'Theo dõi duyệt, phát hành và thu các khoản phí trong quy trình.'), ('Vận hành có dấu vết', 'Quản lý hồ sơ kỹ thuật, checklist và xem báo cáo, lịch sử thao tác.')],
     [('Lập danh mục', 'Chuẩn bị tòa nhà, không gian quản lý và người phụ trách.'), ('Cập nhật định kỳ', 'Ghi chỉ số, rà hồ sơ và xử lý kỳ phí theo quyền.'), ('Theo dõi vận hành', 'Kiểm tra khoản thu và các mục cần được chăm sóc tiếp.')],
     [('Khu căn hộ', 'Tổ chức hồ sơ và các kỳ thu phí.'), ('Tòa nhà doanh nghiệp', 'Theo dõi không gian và công việc vận hành.'), ('Đơn vị quản lý', 'Thống nhất cách ghi nhận giữa các nhân sự.')],
     'Cần xác nhận biểu phí và phạm vi kết nối khi triển khai. Dữ liệu DEMO dùng để trải nghiệm; thanh toán, hóa đơn điện tử và một số tích hợp ngoài cần được trao đổi riêng.'],
    ['Building management', 'Thoughtful operations.\nCalmer working days.',
     'GitGam Building brings property records, meter readings and operating work together, helping management teams care for buildings with a more organized routine.',
     'Building managers, property operators and businesses managing multiple properties.',
     [('Records together', 'Keep property structures, units and related records organized.'), ('Readings & fee periods', 'Record meters, prepare fee periods and follow amounts due.'), ('Visible collections', 'Follow review, issue and collection stages within the fee workflow.'), ('An operational trail', 'Manage technical records and checklists, with reports and activity history.')],
     [('Build your catalog', 'Prepare buildings, managed spaces and responsible people.'), ('Keep records current', 'Update readings, review files and process fee periods within assigned permissions.'), ('Review operations', 'Follow collections and identify items needing attention.')],
     [('Residential properties', 'Organize unit records and recurring fee periods.'), ('Business buildings', 'Keep spaces and operating work in view.'), ('Management providers', 'Give staff a consistent way to record daily work.')],
     'Confirm tariffs and connected services during implementation. DEMO data is for exploration; payments, e-invoices and some external integrations require a separate scope discussion.'])

add('Council', 'GitGam Council', 'people', 'violet',
    ['README.md', 'planning/domain-contract.json'],
    ['Kết nối & phát triển nghề nghiệp', 'Kết nối đúng người.\nMở thêm cơ hội.',
     'GitGam Council tạo không gian để đội ngũ giới thiệu năng lực, chia sẻ tri thức và nuôi dưỡng quan hệ nghề nghiệp. Doanh nghiệp có thêm một cách xây dựng cộng đồng quanh con người của mình.',
     'Doanh nghiệp, cộng đồng chuyên môn, đội tuyển dụng và nhóm cố vấn.',
     [('Hồ sơ & CV', 'Tổ chức kinh nghiệm, thành tựu và các phiên bản CV đã phát hành.'), ('Kết nối có chọn lọc', 'Gửi lời kết nối, tham gia nhóm và chia sẻ bài viết theo phạm vi phù hợp.'), ('Cơ hội & ứng tuyển', 'Theo dõi cơ hội, hồ sơ ứng tuyển và lịch phỏng vấn.'), ('Sự kiện & cố vấn', 'Quản lý đăng ký sự kiện, lịch hẹn cố vấn và tài liệu chia sẻ.')],
     [('Giới thiệu năng lực', 'Hoàn thiện hồ sơ và chuẩn bị CV muốn chia sẻ.'), ('Chọn cộng đồng', 'Kết nối đồng nghiệp, tham gia nhóm hoặc tìm cơ hội phù hợp.'), ('Nuôi dưỡng quan hệ', 'Chia sẻ kiến thức, đăng ký sự kiện và đặt lịch cố vấn.')],
     [('Cộng đồng doanh nghiệp', 'Giữ kết nối giữa nhân viên và mạng lưới chuyên môn.'), ('Tuyển dụng', 'Tổ chức trao đổi về ứng viên và cơ hội.'), ('Nhóm cố vấn', 'Tạo nhịp gặp gỡ và chia sẻ kinh nghiệm.')],
     'Hồ sơ và tài liệu riêng chỉ được chia sẻ trong phạm vi đã cấp. CV đã phát hành được giữ theo phiên bản; thay đổi nội dung cần tạo bản mới.'],
    ['Professional communities', 'Connect with people.\nMake room for opportunity.',
     'GitGam Council gives teams a place to present their experience, exchange knowledge and build professional relationships. Businesses can grow a community around their people.',
     'Businesses, professional communities, recruiting teams and mentoring groups.',
     [('Profiles & CVs', 'Organize experience, achievements and published CV versions.'), ('Intentional connections', 'Connect with peers, join groups and share posts with an appropriate audience.'), ('Opportunities & applications', 'Follow opportunities, applications and interview arrangements.'), ('Events & mentoring', 'Manage event registrations, mentoring bookings and shared documents.')],
     [('Introduce your experience', 'Complete your profile and prepare a CV to share.'), ('Find your community', 'Connect with colleagues, join groups or explore relevant opportunities.'), ('Keep relationships growing', 'Share knowledge, join events and book mentoring time.')],
     [('Business communities', 'Keep people connected with a professional network.'), ('Recruiting teams', 'Organize conversations around candidates and opportunities.'), ('Mentoring groups', 'Create a rhythm for sharing experience.')],
     'Private profiles and documents are shared within granted access. Published CVs are preserved as versions; changes require a new edition.'])

add('Workspace', 'GitGam Workspace', 'board', 'teal',
    ['web/src/route.js', 'web/src/pages/TaskBoard', 'web/src/pages/Gantt', 'web/src/pages/OKR', 'web/src/pages/Wiki'],
    ['Cộng tác & quản lý công việc', 'Cùng một mục tiêu.\nRõ từng bước tiến.',
     'GitGam Workspace giúp doanh nghiệp và đội nhóm cùng nhìn thấy công việc, người phụ trách và tiến độ. Từ kế hoạch đến trao đổi hằng ngày, mọi người có thêm khoảng trống để tập trung vào điều quan trọng.',
     'Đội dự án, phòng ban vận hành, nhóm sản phẩm và doanh nghiệp nhiều đội nhóm.',
     [('Công việc & tiến độ', 'Tổ chức nhiệm vụ, bảng công việc, sprint và mốc dự án.'), ('Kế hoạch cùng mục tiêu', 'Theo dõi lịch, Gantt và OKR để kết nối việc hằng ngày với hướng đi chung.'), ('Tri thức của đội', 'Lưu tài liệu, wiki và thông báo để thông tin có chỗ tìm lại.'), ('Nhịp làm việc rõ hơn', 'Ghi nhận thời gian, báo cáo ngày và theo dõi vấn đề, rủi ro.')],
     [('Tạo không gian chung', 'Chuẩn bị dự án, thành viên và vai trò.'), ('Chia nhỏ kế hoạch', 'Tạo công việc, giao người phụ trách và đặt mốc hoàn thành.'), ('Cùng cập nhật', 'Ghi tiến độ, trao đổi và nhìn lại kết quả trong đội.')],
     [('Đội dự án', 'Phối hợp nhiều người quanh một kế hoạch.'), ('Phòng ban', 'Duy trì nhịp công việc và báo cáo định kỳ.'), ('Quản lý doanh nghiệp', 'Nhìn tiến độ, nguồn lực và các điểm cần hỗ trợ.')],
     'Doanh nghiệp chọn các phân hệ phù hợp để bắt đầu; quyền truy cập và phạm vi sử dụng được thiết lập theo tổ chức.'],
    ['Teamwork & work management', 'A shared direction.\nVisible steps forward.',
     'GitGam Workspace helps businesses and teams see the work, its owners and its progress together. From planning to daily conversations, it creates more room to focus on what matters.',
     'Project teams, operating departments, product groups and businesses with several teams.',
     [('Tasks & progress', 'Organize tasks, boards, sprints and project milestones.'), ('Plans with purpose', 'Use calendars, Gantt views and OKRs to connect daily work with shared goals.'), ('Team knowledge', 'Keep documents, wikis and announcements somewhere people can return to.'), ('A clearer work rhythm', 'Record time and daily updates while following issues and risks.')],
     [('Prepare a shared space', 'Set up a project, invite members and assign roles.'), ('Break down the plan', 'Create tasks, name owners and set completion milestones.'), ('Keep each other informed', 'Update progress, exchange feedback and review results together.')],
     [('Project teams', 'Coordinate several people around one plan.'), ('Departments', 'Maintain recurring work and reporting routines.'), ('Business managers', 'Follow progress, resources and areas needing support.')],
     'Start with the modules that fit your organization. Access and usage scope are configured for your team.'])

add('DevOps', 'GitGam DevOps', 'code', 'blue',
    ['README.md', 'web/src/pages/DefaultLayout/NavigationBar/index.jsx', 'web/src/pages/CICD', 'web/src/pages/PostAPI', 'web/src/pages/VMMachine'],
    ['Phát triển & vận hành phần mềm', 'Từ ý tưởng đến bản phát hành.\nCả đội cùng nhịp.',
     'GitGam DevOps giúp đội phát triển tập hợp mã nguồn, tài liệu API, kiểm thử và quy trình phát hành trong một không gian chung, để việc bàn giao giữa các vai trò rõ ràng hơn.',
     'Doanh nghiệp phần mềm, đội kỹ thuật nội bộ và nhóm phát triển sản phẩm.',
     [('Mã nguồn có tổ chức', 'Quản lý kho mã và theo dõi nội dung theo dự án.'), ('API dễ trao đổi', 'Tổ chức yêu cầu và tài liệu API để các thành viên cùng tham khảo.'), ('Kiểm thử có kế hoạch', 'Quản lý testcase và những việc cần kiểm tra trước bàn giao.'), ('Phát hành & môi trường', 'Thiết lập công việc CI/CD và quản lý máy ảo trong phạm vi được cấp.')],
     [('Chuẩn bị dự án', 'Tạo không gian, kết nối kho mã và phân quyền đội ngũ.'), ('Thống nhất quy trình', 'Tổ chức API, testcase và các bước phát hành.'), ('Theo dõi mỗi lần bàn giao', 'Xem kết quả thực thi và xử lý các việc còn lại.')],
     [('Nhóm sản phẩm', 'Giữ mã nguồn và hoạt động phát triển gần nhau.'), ('Đội kỹ thuật doanh nghiệp', 'Chuẩn hóa cách kiểm thử và bàn giao nội bộ.'), ('Nhóm vận hành', 'Theo dõi môi trường và các bước phát hành được cấu hình.')],
     'CI/CD và máy ảo cần môi trường, quyền truy cập và cấu hình phù hợp. Doanh nghiệp thống nhất quy trình trước khi đưa vào vận hành.'],
    ['Software delivery & operations', 'From ideas to releases.\nMoving together.',
     'GitGam DevOps brings source repositories, API documentation, testing and release work into a shared space, helping development teams make handovers clearer.',
     'Software businesses, internal engineering teams and product development groups.',
     [('Organized source', 'Manage repositories and explore project code.'), ('Shared API knowledge', 'Organize API requests and documentation for the team.'), ('Planned testing', 'Keep test cases and pre-handover checks in view.'), ('Releases & environments', 'Configure CI/CD work and manage virtual machines within assigned access.')],
     [('Prepare a project', 'Create the space, connect repositories and assign team permissions.'), ('Agree on the workflow', 'Organize APIs, test cases and release steps.'), ('Follow each handover', 'Review execution results and address remaining work.')],
     [('Product teams', 'Keep source code and development activity close together.'), ('Business engineering teams', 'Establish consistent testing and internal handovers.'), ('Operations teams', 'Follow configured environments and release steps.')],
     'CI/CD and virtual machines need suitable environments, permissions and configuration. Agree on the operating workflow before adopting them.'])

add('HRM', 'GitGam HRM', 'people', 'coral',
    ['README.md', 'web/src/pages/HRM'],
    ['Nhân sự & phát triển đội ngũ', 'Hiểu đội ngũ hơn.\nĐồng hành dài lâu.',
     'GitGam HRM giúp doanh nghiệp chăm sóc hành trình nhân sự từ tuyển dụng đến công việc hằng ngày. Hồ sơ, chấm công và các yêu cầu được tổ chức để HR và nhân viên phối hợp nhẹ nhàng hơn.',
     'Phòng nhân sự, quản lý bộ phận và doanh nghiệp đang phát triển đội ngũ.',
     [('Con người & tổ chức', 'Quản lý hồ sơ, hợp đồng và cơ cấu nhân sự.'), ('Tuyển dụng & phát triển', 'Theo dõi tuyển dụng và các hoạt động phát triển đội ngũ.'), ('Thời gian & tiền lương', 'Ghi nhận công, duyệt điều chỉnh và chuẩn bị kỳ lương từ dữ liệu đã nhập.'), ('Tự phục vụ & phê duyệt', 'Nhân viên gửi yêu cầu, xem phiếu lương đã duyệt và theo dõi phản hồi.')],
     [('Chuẩn bị hồ sơ', 'Thiết lập tổ chức, nhân sự và quyền theo vai trò.'), ('Thiết lập nhịp xử lý', 'Thống nhất dữ liệu công, kỳ lương và người phê duyệt.'), ('Cùng sử dụng mỗi ngày', 'Nhân viên gửi yêu cầu; HR kiểm tra, duyệt và theo dõi báo cáo.')],
     [('Đội HR', 'Giảm việc tìm hồ sơ ở nhiều nơi.'), ('Quản lý bộ phận', 'Nắm yêu cầu và tình hình nhân sự trong phạm vi phụ trách.'), ('Doanh nghiệp tăng trưởng', 'Xây nền tảng quản lý khi đội ngũ mở rộng.')],
     'Thuế, bảo hiểm, phụ cấp và khấu trừ cần được HR nhập và kiểm tra theo chính sách áp dụng trước khi duyệt lương.'],
    ['People & team development', 'Understand your people.\nGrow together.',
     'GitGam HRM helps businesses care for the employee journey, from recruitment to everyday work. Organized records, attendance and requests make collaboration between HR and employees feel easier.',
     'HR departments, department managers and businesses growing their teams.',
     [('People & organization', 'Maintain employee profiles, contracts and organizational records.'), ('Recruitment & development', 'Follow hiring and team development activities.'), ('Time & payroll', 'Record attendance, approve corrections and prepare payroll from entered information.'), ('Self-service & approvals', 'Employees submit requests, view approved payslips and follow responses.')],
     [('Prepare people records', 'Set up the organization, employee profiles and role access.'), ('Agree on routines', 'Define attendance inputs, payroll periods and reviewers.'), ('Use it together daily', 'Employees raise requests; HR reviews, approves and follows reports.')],
     [('HR teams', 'Spend less time looking for scattered records.'), ('Department managers', 'Follow requests and people matters within their scope.'), ('Growing businesses', 'Build a foundation as the team expands.')],
     'HR should enter and verify tax, insurance, allowances and deductions under the applicable policies before approving payroll.'])

add('OfficeAdmin', 'GitGam OfficeAdmin', 'document', 'coral',
    ['README.md', 'web/src/pages/OfficeAdmin'],
    ['Hành chính & văn phòng', 'Văn phòng gọn gàng.\nCộng tác nhẹ nhàng.',
     'GitGam OfficeAdmin giúp đội hành chính kết nối hồ sơ, đề nghị và nguồn lực văn phòng. Mỗi yêu cầu có người xử lý, mỗi tài sản có nơi theo dõi, để cả doanh nghiệp làm việc thuận hơn.',
     'Phòng hành chính, đội văn phòng và doanh nghiệp có nhiều nhu cầu phục vụ nội bộ.',
     [('Văn bản & lưu trữ', 'Theo dõi văn bản đến, đi, nội bộ, hồ sơ và mượn trả.'), ('Đề nghị & phê duyệt', 'Gửi yêu cầu, chuyển người duyệt và theo dõi trạng thái xử lý.'), ('Tài sản & không gian', 'Quản lý bàn giao tài sản, vật tư, phòng họp và đặt chỗ.'), ('Chi phí & dịch vụ', 'Theo dõi ngân sách, nhà cung cấp, chi phí và các dịch vụ văn phòng.')],
     [('Sắp xếp danh mục', 'Chuẩn bị tài sản, không gian, hồ sơ và người phụ trách.'), ('Thống nhất luồng duyệt', 'Chọn người xét duyệt và cách xử lý từng nhóm yêu cầu.'), ('Đưa vào công việc', 'Nhân viên gửi đề nghị; hành chính xử lý, bàn giao và đối chiếu.')],
     [('Vận hành văn phòng', 'Đặt phòng, quản lý vật tư và tài sản có tổ chức.'), ('Văn thư', 'Theo dõi văn bản và hồ sơ phát hành.'), ('Dịch vụ nội bộ', 'Tạo một nơi rõ ràng để nhân viên gửi đề nghị.')],
     'Quy trình trình ký và sổ đóng dấu là quản lý nghiệp vụ nội bộ; không mặc nhiên thay thế dịch vụ chữ ký số bên ngoài.'],
    ['Administration & office work', 'An organized office.\nAn easier working day.',
     'GitGam OfficeAdmin connects office records, requests and shared resources. With owners for requests and a place to track assets, business administration becomes easier to coordinate.',
     'Administration departments, office teams and businesses supporting internal service needs.',
     [('Documents & archives', 'Track incoming, outgoing and internal documents, files and borrowing.'), ('Requests & approvals', 'Submit requests, route reviews and follow their progress.'), ('Assets & spaces', 'Manage asset handovers, supplies, meeting rooms and bookings.'), ('Costs & services', 'Follow budgets, vendors, expenses and office services.')],
     [('Organize your catalogs', 'Prepare assets, spaces, files and responsible people.'), ('Agree on approvals', 'Choose reviewers and the process for each request type.'), ('Make it part of the day', 'Employees submit requests; administration handles and reconciles them.')],
     [('Office operations', 'Organize room bookings, supplies and assets.'), ('Document teams', 'Follow official records and issued documents.'), ('Internal services', 'Give employees a clear place to ask for support.')],
     'Internal signing and sealing registers support administrative workflows; they do not automatically replace an external digital-signature service.'])

add('HelpDesk', 'GitGam HelpDesk', 'support', 'blue',
    ['domain/catalog.json', 'web/src/pages/Tickets', 'api/src/utils/hdDomain.js'],
    ['Dịch vụ & hỗ trợ', 'Mỗi yêu cầu được lắng nghe.\nMỗi việc có người đồng hành.',
     'GitGam HelpDesk giúp doanh nghiệp tiếp nhận, phân công và theo dõi yêu cầu hỗ trợ có tổ chức. Đội dịch vụ có thêm bối cảnh để xử lý, người gửi có nơi để theo dõi tiến trình.',
     'Đội IT, kỹ thuật, bảo trì và các bộ phận cung cấp dịch vụ nội bộ.',
     [('Yêu cầu & sự cố', 'Ghi nội dung, mức ưu tiên, người xử lý và các trao đổi liên quan.'), ('Điều phối đội ngũ', 'Sắp ca trực, lịch hẹn và theo dõi thợ, kỹ thuật viên.'), ('Nguồn lực xử lý', 'Ghi vật tư, dụng cụ, chi phí và thời gian thực hiện.'), ('Tri thức & chất lượng', 'Lưu hướng dẫn, đặt chính sách thời gian phục vụ và theo dõi KPI.')],
     [('Chuẩn bị dịch vụ', 'Lập danh mục hỗ trợ, đội xử lý và chính sách phục vụ.'), ('Tiếp nhận & phân công', 'Tạo yêu cầu, chọn người phụ trách và lịch xử lý.'), ('Hoàn tất & học hỏi', 'Cập nhật kết quả, đóng yêu cầu và lưu kinh nghiệm hữu ích.')],
     [('IT nội bộ', 'Theo dõi sự cố thiết bị và nhu cầu hỗ trợ.'), ('Đội kỹ thuật', 'Phối hợp lịch hẹn, vật tư và công việc hiện trường.'), ('Trung tâm dịch vụ', 'Quan sát chất lượng và khối lượng xử lý của đội.')],
     'Chỉ tiêu thời gian phục vụ được doanh nghiệp thiết lập; đây là công cụ theo dõi công việc, không phải cam kết dịch vụ mặc định từ nhà cung cấp.'],
    ['Service & support', 'Every request heard.\nEvery task with an owner.',
     'GitGam HelpDesk gives businesses an organized way to receive, assign and follow support requests. Service teams gain context, while requesters have somewhere to follow progress.',
     'IT, technical support, maintenance and internal service departments.',
     [('Requests & incidents', 'Record details, priorities, owners and related conversations.'), ('Team coordination', 'Arrange shifts and appointments while organizing technicians.'), ('Service resources', 'Record materials, tools, costs and time spent.'), ('Knowledge & quality', 'Keep helpful guides, define service-time policies and follow KPIs.')],
     [('Prepare your services', 'Set up service categories, support teams and service policies.'), ('Receive & assign', 'Create requests, choose owners and plan the work.'), ('Complete & learn', 'Record outcomes, close requests and keep useful knowledge.')],
     [('Internal IT', 'Follow equipment incidents and assistance requests.'), ('Technical teams', 'Coordinate appointments, materials and field work.'), ('Service centers', 'Review team workload and service quality.')],
     'Service-time targets are defined by your business. These tracking policies are not a default service guarantee from the provider.'])

add('Marketing', 'GitGam Marketing', 'megaphone', 'coral',
    ['domain/catalog.json', 'api/src/utils/mkDomain.js', 'web/src/pages/Automation'],
    ['Marketing & chăm sóc khách hàng', 'Gần khách hàng hơn.\nCó hướng đi cho mỗi chiến dịch.',
     'GitGam Marketing giúp doanh nghiệp kết nối kế hoạch, nội dung và chăm sóc khách hàng. Cả đội có thể nhìn lại mình đang tiếp cận ai, làm gì tiếp theo và dùng ngân sách ra sao.',
     'Phòng marketing, đội chăm sóc khách hàng và nhóm kinh doanh phối hợp chiến dịch.',
     [('Kế hoạch & ngân sách', 'Tổ chức chiến dịch, ngân sách và chi phí theo hoạt động.'), ('Khách hàng có bối cảnh', 'Quản lý đầu mối, doanh nghiệp, phân khúc và lịch sử tương tác.'), ('Nội dung & lịch', 'Chuẩn bị nội dung và theo dõi các bước duyệt, lên lịch.'), ('Chăm sóc có nhịp', 'Theo dõi việc cần làm, lịch hẹn, cơ hội và kịch bản chăm sóc.')],
     [('Xác định mục tiêu', 'Chuẩn bị đối tượng, chiến dịch và ngân sách.'), ('Cùng triển khai', 'Phân công nội dung, ghi tương tác và theo dõi công việc chăm sóc.'), ('Nhìn lại kết quả', 'Xem báo cáo, KPI và điều chỉnh cách tiếp cận của đội.')],
     [('Marketing doanh nghiệp', 'Phối hợp kế hoạch với hoạt động thực tế.'), ('Đội chăm sóc', 'Giữ thông tin tương tác để tiếp nối cuộc trò chuyện.'), ('Nhóm tăng trưởng', 'Theo dõi cơ hội và nhu cầu khách hàng có tổ chức.')],
     'Các kết nối gửi email, SMS, quảng cáo hoặc xuất bản bên ngoài cần được xác nhận riêng. Lịch và hàng đợi trong ứng dụng không đồng nghĩa nội dung đã được gửi ra ngoài.'],
    ['Marketing & customer care', 'Closer to customers.\nA direction for every campaign.',
     'GitGam Marketing connects plans, content and customer care. Teams can see whom they are reaching, what comes next and how their activity relates to the budget.',
     'Marketing departments, customer care teams and sales groups working on campaigns.',
     [('Plans & budgets', 'Organize campaigns, budgets and activity costs.'), ('Customers with context', 'Manage leads, companies, segments and interaction history.'), ('Content & calendars', 'Prepare content and follow review and scheduling stages.'), ('A rhythm for customer care', 'Follow tasks, appointments, opportunities and care playbooks.')],
     [('Define your goal', 'Prepare audiences, campaigns and budgets.'), ('Work as a team', 'Assign content, record interactions and follow care tasks.'), ('Reflect on results', 'Review reports and KPIs, then refine the team’s approach.')],
     [('Business marketing', 'Connect planning with day-to-day activity.'), ('Customer care teams', 'Keep context to continue the conversation.'), ('Growth teams', 'Organize opportunities and customer needs.')],
     'External email, SMS, advertising and publishing connections need separate confirmation. Scheduling and queues inside the application do not mean content has been sent externally.'])

add('Producing', 'GitGam Producing', 'factory', 'teal',
    ['domain/catalog.json', 'api/src/utils/prDomain.js', 'web/src/pages/Traceability'],
    ['Sản xuất & quản lý nhà máy', 'Nhịp nhà máy rõ hơn.\nĐội ngũ phối hợp tốt hơn.',
     'GitGam Producing giúp doanh nghiệp nối kế hoạch với lệnh sản xuất, vật tư và chất lượng. Mỗi bộ phận có thêm thông tin để phối hợp, từ chuẩn bị nguyên liệu đến nhìn lại kết quả.',
     'Doanh nghiệp sản xuất, xưởng, đội kế hoạch, kho và quản lý chất lượng.',
     [('Kế hoạch & lệnh', 'Lập kế hoạch, định mức nguyên liệu và quy trình công đoạn.'), ('Vật tư & kho', 'Theo dõi nhu cầu, cấp trả vật tư, lô hàng và luân chuyển kho.'), ('Thực thi & chất lượng', 'Ghi nhận sản lượng, kiểm tra chất lượng và xử lý điểm không phù hợp.'), ('Thiết bị & giá thành', 'Theo dõi bảo trì, nhân lực và tính giá thành từ dữ liệu được ghi nhận.')],
     [('Chuẩn bị nền sản xuất', 'Khai báo sản phẩm, định mức, công đoạn và kho.'), ('Điều phối thực hiện', 'Duyệt kế hoạch, cấp vật tư và cập nhật tiến độ từng lệnh.'), ('Kiểm tra & hoàn tất', 'Xác nhận chất lượng, rà số liệu và nhìn lại chi phí.')],
     [('Xưởng sản xuất', 'Tạo một luồng thông tin từ kế hoạch đến thực hiện.'), ('Đội kho', 'Phối hợp cấp vật tư và theo dõi lô.'), ('Quản lý chất lượng', 'Lưu kết quả kiểm tra và việc khắc phục.')],
     'Dữ liệu vận hành được nhập và xử lý theo quy trình đã cấu hình; kết nối máy móc hoặc hệ thống ngoài cần thống nhất riêng khi triển khai.'],
    ['Manufacturing & factory management', 'A clearer factory rhythm.\nBetter coordination.',
     'GitGam Producing connects plans with manufacturing orders, materials and quality records. Departments gain more context to work together, from material preparation to reviewing results.',
     'Manufacturing businesses, workshops, planning teams, warehouses and quality teams.',
     [('Plans & orders', 'Prepare production plans, material requirements and process routes.'), ('Materials & warehouse', 'Follow demand, issues, returns, lots and stock transfers.'), ('Execution & quality', 'Record output, inspect quality and address nonconformities.'), ('Equipment & costing', 'Track maintenance, workforce and costing based on recorded inputs.')],
     [('Prepare the foundation', 'Define products, material lists, process steps and warehouses.'), ('Coordinate production', 'Approve plans, issue materials and update order progress.'), ('Check & complete', 'Confirm quality, review figures and examine costs.')],
     [('Workshops', 'Create an information flow from planning to execution.'), ('Warehouse teams', 'Coordinate material supply and lot tracking.'), ('Quality teams', 'Keep inspection results and corrective actions together.')],
     'Operating information is entered and processed through configured workflows. Machine and external-system connections need a separate implementation scope.'])

add('Store', 'GitGam Store', 'shop', 'coral',
    ['README.md', 'docs/store-commerce.md', 'docs/store-sales-operations.md', 'docs/websites.md'],
    ['Bán hàng & hiện diện số', 'Chăm từng đơn hàng.\nKể câu chuyện thương hiệu.',
     'GitGam Store giúp doanh nghiệp tổ chức sản phẩm, khách hàng và nội dung trên cùng một nền tảng. Đội bán hàng và nội dung có thêm một nơi chung để xây trải nghiệm thương hiệu.',
     'Doanh nghiệp thương mại, cửa hàng, thương hiệu và đội vận hành bán hàng.',
     [('Sản phẩm & tồn kho', 'Quản lý danh mục, thông tin sản phẩm, mua hàng và kho.'), ('Khách hàng & đơn hàng', 'Theo dõi hồ sơ khách, đơn hàng và các bước xử lý bán hàng.'), ('Nội dung & tài nguyên', 'Tổ chức bài viết, hình ảnh, tài liệu và nội dung cộng đồng.'), ('Website & báo cáo', 'Quản lý website theo cấu hình và xem các báo cáo phục vụ vận hành.')],
     [('Chuẩn bị cửa hàng', 'Nhập sản phẩm, danh mục và thông tin doanh nghiệp.'), ('Xây nội dung', 'Chuẩn bị tài nguyên, bài viết và website phù hợp thương hiệu.'), ('Vận hành mỗi ngày', 'Theo dõi khách, đơn hàng, hàng hóa và dữ liệu hoạt động.')],
     [('Cửa hàng doanh nghiệp', 'Kết nối danh mục hàng với công việc xử lý đơn.'), ('Đội nội dung', 'Giữ tài nguyên và bài viết có tổ chức.'), ('Thương hiệu', 'Xây điểm chạm trực tuyến cùng dữ liệu vận hành.')],
     'Thanh toán, vận chuyển, kênh bán ngoài và gửi chiến dịch phụ thuộc kết nối được triển khai. Dữ liệu thống kê cần được đọc đúng nguồn khách hoặc hoạt động nội bộ.'],
    ['Commerce & digital presence', 'Care for every order.\nTell your brand’s story.',
     'GitGam Store brings products, customers and content into one platform. Sales and content teams gain a shared place to build a more consistent brand experience.',
     'Trading businesses, stores, brands and sales operations teams.',
     [('Products & stock', 'Manage catalogs, product information, purchasing and inventory.'), ('Customers & orders', 'Follow customer records, orders and sales processing stages.'), ('Content & resources', 'Organize articles, images, documents and community content.'), ('Websites & reporting', 'Manage websites within the configured setup and review operating reports.')],
     [('Prepare your store', 'Enter products, categories and business information.'), ('Build your content', 'Prepare resources, articles and a website suited to your brand.'), ('Run daily operations', 'Follow customers, orders, stock and recorded activity.')],
     [('Business stores', 'Connect the product catalog with order handling.'), ('Content teams', 'Keep resources and articles organized.'), ('Brands', 'Build online touchpoints alongside operating information.')],
     'Payments, shipping, outside sales channels and campaign sending depend on implemented connections. Read analytics in the context of customer or internal activity sources.'])

add('Insight', 'GitGam Insight', 'spark', 'violet',
    ['web/src/insight/catalog.js', 'web/src/pages/Community', 'api/src/route'],
    ['Cộng đồng & truyền thông nội bộ', 'Câu chuyện được sẻ chia.\nĐội ngũ thêm gắn kết.',
     'GitGam Insight giúp doanh nghiệp tạo không gian chia sẻ tin tức, ý tưởng và sự ghi nhận. Những điều đáng biết có chỗ để được đọc, thảo luận và tìm lại trong đội.',
     'Doanh nghiệp, đội truyền thông nội bộ và các cộng đồng đội nhóm.',
     [('Bảng tin của đội', 'Chia sẻ thông báo, tin nội bộ, sự kiện và bài viết.'), ('Kênh theo chủ đề', 'Khám phá, theo dõi kênh và chọn nội dung quan tâm.'), ('Tương tác & ghi nhận', 'Trao đổi, bình chọn và gửi lời ghi nhận đến đồng đội.'), ('Tổ chức nội dung', 'Lưu bài, theo dõi thông báo và quản lý nội dung theo quyền.')],
     [('Mở kênh phù hợp', 'Chuẩn bị các chủ đề cho doanh nghiệp hoặc đội nhóm.'), ('Mời mọi người tham gia', 'Theo dõi kênh, đăng chia sẻ và trao đổi.'), ('Duy trì nhịp kết nối', 'Cập nhật tin, ghi nhận đóng góp và chọn lọc nội dung hữu ích.')],
     [('Truyền thông nội bộ', 'Tạo nơi để thông báo và câu chuyện doanh nghiệp dễ tìm.'), ('Nhóm chuyên môn', 'Trao đổi ý tưởng quanh từng chủ đề.'), ('Văn hóa doanh nghiệp', 'Ghi nhận đóng góp và khuyến khích chia sẻ.')],
     'Nội dung và công cụ kiểm duyệt hiển thị theo vai trò được cấp trong tổ chức.'],
    ['Communities & internal communication', 'Stories worth sharing.\nTeams that feel connected.',
     'GitGam Insight gives businesses a space for news, ideas and recognition. Useful updates have somewhere to be read, discussed and revisited by the team.',
     'Businesses, internal communication teams and workplace communities.',
     [('A team feed', 'Share announcements, internal news, events and posts.'), ('Channels by topic', 'Discover and follow channels that matter to your work.'), ('Interaction & appreciation', 'Discuss, take polls and recognize colleagues.'), ('Organized content', 'Save posts, follow notifications and manage content within assigned roles.')],
     [('Prepare useful channels', 'Choose topics for your business or teams.'), ('Bring people together', 'Follow channels, publish updates and join conversations.'), ('Keep the connection alive', 'Share news, recognize contributions and curate useful content.')],
     [('Internal communication', 'Make business news and stories easier to find.'), ('Professional groups', 'Exchange ideas around shared topics.'), ('Workplace culture', 'Recognize contributions and encourage participation.')],
     'Available content and moderation tools follow the roles assigned within your organization.'])

add('Mailing', 'GitGam Mail', 'mail', 'blue',
    ['web/src/pages/Mail/components/Sidebar.jsx', 'web/src/pages/Mail/components/MailServer.jsx', 'api/src/utils/mailingAdmin.js'],
    ['Email doanh nghiệp', 'Hộp thư gọn hơn.\nTrao đổi liền mạch hơn.',
     'GitGam Mail mang đến không gian email cho công việc doanh nghiệp. Đọc, soạn và sắp xếp thư trong một giao diện thống nhất, để đội ngũ giữ được mạch trao đổi với đồng nghiệp và đối tác.',
     'Doanh nghiệp dùng email theo tên miền và đội nhóm cần tổ chức trao đổi công việc.',
     [('Đọc & soạn thư', 'Theo dõi chuỗi trao đổi, trả lời và chuẩn bị thư mới.'), ('Sắp xếp theo cách của bạn', 'Dùng thư mục, nhãn, gắn sao và tìm kiếm để tìm lại nội dung.'), ('Quản lý nhịp xử lý', 'Theo dõi bản nháp, thư đang gửi, lưu trữ và thư rác.'), ('Quản trị theo doanh nghiệp', 'Quản lý hộp thư, tên miền và hạn mức theo quyền được cấp.')],
     [('Chuẩn bị email', 'Người quản trị cấu hình tên miền, dịch vụ thư và thành viên.'), ('Tổ chức hộp thư', 'Tạo thư mục, nhãn và cách phân loại phù hợp.'), ('Dùng trong công việc', 'Đọc, gửi, tìm lại thư và theo dõi trạng thái xử lý.')],
     [('Trao đổi đối tác', 'Giữ email công việc trong không gian của doanh nghiệp.'), ('Đội ngũ nội bộ', 'Tổ chức nội dung và tìm lại trao đổi.'), ('Quản trị email', 'Theo dõi cấu hình và hạn mức hộp thư.')],
     'Gửi và nhận thư cần tên miền, DNS và máy chủ thư được cấu hình đúng. Phạm vi hộp thư và dung lượng được thống nhất theo gói triển khai.'],
    ['Business email', 'A tidier inbox.\nConversations that flow.',
     'GitGam Mail offers a business email workspace for reading, writing and organizing messages. A consistent interface helps teams keep conversations with colleagues and partners in context.',
     'Businesses using domain email and teams organizing work conversations.',
     [('Read & compose', 'Follow conversation threads, reply and prepare new messages.'), ('Organize your way', 'Use folders, labels, stars and search to return to useful messages.'), ('Follow message handling', 'Keep drafts, outgoing messages, archives and spam in view.'), ('Business administration', 'Manage mailboxes, domains and quotas within assigned permissions.')],
     [('Prepare business email', 'An administrator configures domains, mail services and members.'), ('Organize the inbox', 'Create folders, labels and categories that fit your work.'), ('Use it every day', 'Read, send, find messages and follow their status.')],
     [('Partner communication', 'Keep business email within your organization’s workspace.'), ('Internal teams', 'Organize content and return to past conversations.'), ('Email administrators', 'Follow mailbox configuration and quotas.')],
     'Sending and receiving require correctly configured domains, DNS and mail servers. Mailbox scope and capacity are agreed as part of implementation.'])

add('Messenger', 'GitGam Messenger', 'chat', 'violet',
    ['README.md', 'web/src/pages/MessengerWorkspace.jsx', 'web/src/pages/Chatting/calling', 'web/src/pages/MeetingGuest'],
    ['Trao đổi & họp nhóm', 'Gần nhau hơn.\nDù làm việc ở đâu.',
     'GitGam Messenger giúp đội ngũ giữ kết nối qua tin nhắn, chia sẻ và cuộc gọi. Các cuộc trò chuyện công việc có không gian riêng để cả nhóm trao đổi tự nhiên hơn.',
     'Doanh nghiệp, đội dự án, nhóm làm việc kết hợp và các bộ phận cộng tác từ xa.',
     [('Trò chuyện công việc', 'Trao đổi trực tiếp hoặc theo nhóm trong không gian của đội.'), ('Tệp & nội dung', 'Chia sẻ và tìm lại tệp, hình ảnh cùng nội dung trao đổi.'), ('Gọi & họp trực tuyến', 'Kết nối âm thanh, video và các cuộc họp theo cấu hình dịch vụ.'), ('Kết nối người tham gia', 'Tổ chức phòng họp và luồng tham gia dành cho khách được mời.')],
     [('Kết nối đội ngũ', 'Đăng nhập vào tổ chức và tìm đồng nghiệp.'), ('Tạo cuộc trò chuyện', 'Mở trao đổi trực tiếp hoặc nhóm theo công việc.'), ('Trao đổi linh hoạt', 'Gửi nội dung, chia sẻ tệp hoặc chuyển sang cuộc gọi khi cần.')],
     [('Đội dự án', 'Giữ trao đổi nhanh quanh việc đang làm.'), ('Doanh nghiệp phân tán', 'Duy trì kết nối giữa người làm ở nhiều địa điểm.'), ('Họp cộng tác', 'Mời người liên quan vào cuộc trao đổi phù hợp.')],
     'Cuộc gọi cần mạng và quyền camera, microphone phù hợp; khả năng kết nối phụ thuộc thiết bị và cấu hình dịch vụ họp.'],
    ['Team messaging & meetings', 'Feel closer.\nWherever work happens.',
     'GitGam Messenger keeps teams connected through messages, sharing and calls. Work conversations gain a dedicated space where people can collaborate naturally.',
     'Businesses, project teams, hybrid workplaces and remote departments.',
     [('Work conversations', 'Talk directly or in groups within your team’s workspace.'), ('Files & shared content', 'Share and revisit files, images and conversation content.'), ('Calls & online meetings', 'Connect through audio, video and meetings with the configured service.'), ('Invited participants', 'Organize meeting rooms and guest joining for invited people.')],
     [('Connect your team', 'Sign in to your organization and find colleagues.'), ('Start a conversation', 'Open a direct conversation or a work group.'), ('Choose how to connect', 'Send messages, share files or move to a call when useful.')],
     [('Project teams', 'Keep quick conversations close to ongoing work.'), ('Distributed businesses', 'Maintain connections across locations.'), ('Collaborative meetings', 'Bring the right people into the conversation.')],
     'Calls require suitable connectivity and camera or microphone permissions. Connection availability depends on devices and meeting-service configuration.'])

add('Go', 'GitGam Go', 'route', 'coral',
    ['README.md', 'planning/domain-contract.json'],
    ['Điều phối dịch vụ di chuyển & giao nhận', 'Kết nối mỗi hành trình.\nChăm từng lượt giao.',
     'GitGam Go giúp đội vận hành tổ chức chuyến đi, đơn món ăn và giao nhận. Khách hàng, tài xế và người điều phối có thông tin chung để theo dõi từng bước phục vụ.',
     'Doanh nghiệp dịch vụ, đội điều phối, đơn vị giao nhận và đối tác nhà hàng.',
     [('Chuyến & giao nhận', 'Tổ chức yêu cầu chuyến đi, đơn hàng và bưu kiện.'), ('Tài xế & phương tiện', 'Quản lý hồ sơ, tình trạng nhận chuyến và phương tiện.'), ('Nhà hàng & thực đơn', 'Quản lý món ăn, khẩu phần, món thêm và ưu đãi.'), ('Theo dõi & đối soát', 'Cập nhật tiến trình, ghi thu hộ tiền mặt và theo dõi đối soát.')],
     [('Chuẩn bị dịch vụ', 'Khai báo giá, tài xế, phương tiện và nhà hàng theo phạm vi dùng.'), ('Tiếp nhận yêu cầu', 'Tạo chuyến hoặc đơn hàng, xác nhận thông tin và phân công.'), ('Hoàn tất hành trình', 'Cập nhật kết quả, ghi nhận tiền mặt và rà đối soát.')],
     [('Đội điều phối', 'Giữ thông tin chuyến và người thực hiện có tổ chức.'), ('Đơn vị giao nhận', 'Theo dõi bưu kiện cùng các bước xử lý.'), ('Nhóm vận hành nhà hàng', 'Quản lý danh mục và đơn phục vụ.')],
     'Phiên bản hiện tại thanh toán tiền mặt; đối soát không tự chuyển tiền. Báo giá theo tuyến cần dịch vụ định tuyến được cấu hình, và chia sẻ vị trí cần người dùng cho phép.'],
    ['Mobility & delivery operations', 'Connect every journey.\nCare for every delivery.',
     'GitGam Go helps operating teams organize trips, food orders and deliveries. Customers, drivers and coordinators share the context needed to follow each service step.',
     'Service businesses, dispatch teams, delivery operators and restaurant partners.',
     [('Trips & deliveries', 'Organize trip requests, orders and parcels.'), ('Drivers & vehicles', 'Manage driver profiles, availability and vehicles.'), ('Restaurants & menus', 'Maintain dishes, portions, add-ons and promotions.'), ('Tracking & reconciliation', 'Update progress, record cash collection and follow settlements.')],
     [('Prepare your service', 'Define pricing, drivers, vehicles and restaurants as needed.'), ('Receive a request', 'Create a trip or order, confirm details and assign the work.'), ('Complete the journey', 'Update outcomes, record cash and review reconciliation.')],
     [('Dispatch teams', 'Keep journeys and assigned people organized.'), ('Delivery operators', 'Follow parcels and handling stages.'), ('Restaurant operations', 'Organize menus and service orders.')],
     'The current version uses cash payments; reconciliation does not transfer money. Route-based quotes require a configured routing service, and location sharing needs user permission.'])

add('Premium', 'GitGam Premium', 'server', 'blue',
    ['README.md', 'api/docs/SERVICE-MANAGER.md', 'api/docs/CERTIFICATES.md', 'api/docs/MAIL-DNS.md', 'web/src/pages/Status'],
    ['Quản trị nền tảng', 'Nhìn rõ hệ thống.\nChủ động vận hành.',
     'GitGam Premium là không gian quản trị cho người phụ trách nền tảng GitGam. Tập hợp tình trạng tài nguyên, ứng dụng và dịch vụ để đội vận hành có thêm bối cảnh trước mỗi thao tác.',
     'Đội IT doanh nghiệp, quản trị nền tảng và người phụ trách hạ tầng GitGam.',
     [('Tổng quan trạng thái', 'Theo dõi tình trạng máy chủ và tài nguyên được hệ thống ghi nhận.'), ('Ứng dụng & dịch vụ', 'Quản lý các thành phần GitGam và xem nhật ký vận hành.'), ('Kết nối & công cụ', 'Sử dụng kết nối quản trị, terminal và thư mục trong phạm vi được cấp.'), ('Cấu hình nền tảng', 'Theo dõi các mục dữ liệu, sao lưu, chứng chỉ và cấu hình dịch vụ liên quan.')],
     [('Chuẩn bị hạ tầng', 'Thống nhất máy chủ, tài nguyên và phạm vi quản trị.'), ('Kết nối quản trị', 'Đội được cấp quyền mở Premium qua phương thức truy cập đã thiết lập.'), ('Theo dõi có kế hoạch', 'Kiểm tra trạng thái, xem log và thực hiện tác vụ theo quy trình.')],
     [('IT doanh nghiệp', 'Có nơi chung để theo dõi nền tảng.'), ('Vận hành On-premises', 'Quản lý bộ cài trên hạ tầng doanh nghiệp.'), ('Đội cung cấp dịch vụ', 'Tổ chức các việc quản trị môi trường GitGam.')],
     'Premium là công cụ quản trị nền tảng, khác với lựa chọn triển khai On-premises. Thao tác hệ thống cần nhân sự có quyền và quy trình vận hành phù hợp.'],
    ['Platform administration', 'See your platform.\nOperate with clarity.',
     'GitGam Premium is an administration workspace for the people responsible for your GitGam platform. Resource status, applications and services come together to inform operating decisions.',
     'Business IT teams, platform administrators and GitGam infrastructure operators.',
     [('Status overview', 'Follow server and resource conditions recorded by the platform.'), ('Applications & services', 'Manage GitGam components and inspect operating logs.'), ('Connections & tools', 'Use management connections, terminals and directories within assigned access.'), ('Platform configuration', 'Review relevant data services, backups, certificates and service settings.')],
     [('Prepare the environment', 'Agree on servers, resources and the management scope.'), ('Connect administrators', 'Authorized staff open Premium through the configured access method.'), ('Follow an operating routine', 'Review status and logs, then carry out planned tasks.')],
     [('Business IT', 'Give the team a shared view of the platform.'), ('On-premises operations', 'Manage installations on business-owned infrastructure.'), ('Service teams', 'Organize administration of GitGam environments.')],
     'Premium is the platform administration product; On-premises describes a deployment option. System tasks require authorized staff and suitable operating procedures.'])

add('Home', 'GitGam Home', 'home', 'teal',
    ['README.md', 'web/src/pages/Home'],
    ['Khám phá hệ sinh thái GitGam', 'Một điểm bắt đầu.\nNhiều cách cùng phát triển.',
     'GitGam Home là cửa ngõ để doanh nghiệp và đội nhóm tìm hiểu hệ sinh thái GitGam. Khám phá sản phẩm, tham khảo thông tin và chọn hướng bắt đầu phù hợp với cách đội ngũ làm việc.',
     'Chủ doanh nghiệp, quản lý bộ phận và đội nhóm đang tìm giải pháp cộng tác.',
     [('Khám phá sản phẩm', 'Tìm hiểu những không gian làm việc phục vụ từng nhu cầu doanh nghiệp.'), ('Thông tin lựa chọn', 'Tham khảo giới thiệu gói và các thông tin được công bố.'), ('Hướng dẫn & giải đáp', 'Đọc câu hỏi thường gặp, hướng dẫn và thông tin lộ trình.'), ('Kết nối trải nghiệm', 'Đi đến trang tài khoản và khu vực tải ứng dụng phù hợp.')],
     [('Bắt đầu từ nhu cầu', 'Xác định điều đội ngũ muốn cải thiện trong công việc.'), ('Khám phá lựa chọn', 'Đọc giới thiệu sản phẩm và tham khảo hướng dẫn.'), ('Trao đổi cùng GitGam', 'Chọn sản phẩm và cách triển khai phù hợp cho doanh nghiệp.')],
     [('Đánh giá giải pháp', 'Có một nơi để bắt đầu tìm hiểu GitGam.'), ('Giới thiệu nội bộ', 'Chia sẻ thông tin sản phẩm với các bộ phận.'), ('Khởi động sử dụng', 'Tìm điểm truy cập và tài nguyên hướng dẫn.')],
     'Thông tin gói và phạm vi cung cấp cần được xác nhận khi tư vấn. GitGam Home là cổng giới thiệu; việc đăng nhập được thực hiện qua GitGam Account.'],
    ['Discover the GitGam ecosystem', 'One place to begin.\nMore ways to grow together.',
     'GitGam Home is a starting point for businesses and teams exploring GitGam. Discover products, find guidance and choose a direction that suits the way your people work.',
     'Business owners, department managers and teams exploring collaboration tools.',
     [('Discover products', 'Explore workspaces designed around different business needs.'), ('Explore your options', 'Review published plan introductions and product information.'), ('Guidance & answers', 'Read frequently asked questions, tutorials and roadmap information.'), ('Connect to the experience', 'Find the account entry point and application downloads.')],
     [('Start with your needs', 'Identify what your team wants to improve.'), ('Explore the options', 'Read product introductions and practical guidance.'), ('Talk with GitGam', 'Choose suitable products and deployment options for your business.')],
     [('Solution evaluation', 'Find a starting point for understanding GitGam.'), ('Internal introductions', 'Share product information with departments.'), ('Getting started', 'Locate entry points and helpful resources.')],
     'Plans and delivery scope are confirmed during consultation. GitGam Home introduces the platform; sign-in is handled by GitGam Account.'])

add('Desktop-App', 'GitGam Desktop', 'desktop', 'blue',
    ['README.md', 'src', 'test/smoke.cjs'],
    ['Ứng dụng cho máy tính', 'Không gian quen thuộc.\nSẵn sàng cho ngày làm việc.',
     'GitGam Desktop đưa không gian GitGam vào một cửa sổ ứng dụng riêng trên máy tính. Đội ngũ có thêm một cách mở công cụ công việc mà không phải tìm lại giữa nhiều tab trình duyệt.',
     'Doanh nghiệp, đội văn phòng và nhóm kỹ thuật làm việc thường xuyên trên máy tính.',
     [('Cửa sổ dành cho công việc', 'Mở nền tảng GitGam trong ứng dụng desktop riêng.'), ('Trải nghiệm web quen thuộc', 'Sử dụng các chức năng của ứng dụng GitGam được mở bên trong.'), ('Theo môi trường doanh nghiệp', 'Bản cài kết nối tới môi trường được cấu hình cho đội ngũ.'), ('Lựa chọn nền tảng', 'Có công cụ đóng gói cho macOS, Windows và Linux theo cấu hình triển khai.')],
     [('Chọn bản cài phù hợp', 'Nhận bộ cài đúng hệ điều hành và môi trường doanh nghiệp.'), ('Mở không gian làm việc', 'Khởi động ứng dụng và đăng nhập theo quyền được cấp.'), ('Duy trì nhịp làm việc', 'Sử dụng chức năng được bật trong nền tảng GitGam của đội.')],
     [('Đội văn phòng', 'Có lối mở công việc cố định trên máy tính.'), ('Đội kỹ thuật', 'Truy cập môi trường GitGam đã được chuẩn bị.'), ('Doanh nghiệp triển khai tập trung', 'Phân phối bản cài phù hợp cho đội ngũ.')],
     'Chức năng phụ thuộc ứng dụng web và dịch vụ được kết nối. Bản cài được chuẩn bị theo hệ điều hành; không mặc định mọi nghiệp vụ đều hoạt động khi mất mạng.'],
    ['Desktop application', 'A familiar workspace.\nReady for the working day.',
     'GitGam Desktop puts the GitGam workspace in its own computer application window. Teams gain a steady way to open their work tools without searching through browser tabs.',
     'Businesses, office teams and engineering groups working regularly on computers.',
     [('A window for work', 'Open the GitGam platform in a dedicated desktop application.'), ('A familiar web experience', 'Use the features of the GitGam application opened inside.'), ('Your business environment', 'Connect the installed edition to the environment configured for your team.'), ('Platform choices', 'Packaging tools support macOS, Windows and Linux according to the deployment setup.')],
     [('Choose the right installer', 'Obtain the edition for your operating system and business environment.'), ('Open your workspace', 'Launch the application and sign in with assigned access.'), ('Build a daily routine', 'Use the features enabled on your team’s GitGam platform.')],
     [('Office teams', 'Keep a consistent entry point on the computer.'), ('Engineering teams', 'Open a prepared GitGam environment.'), ('Business rollouts', 'Distribute suitable installers to team members.')],
     'Features depend on the connected web application and services. Installers are prepared per platform; offline business functionality is not assumed.'])

add('Mobile-App', 'GitGam Mobile', 'phone', 'violet',
    ['README.md', 'lib/page/home/ui/home_page.dart', 'lib/services/web_device_permissions.dart', 'lib/services/notification_service.dart'],
    ['Ứng dụng cho thiết bị di động', 'Giữ kết nối với đội.\nTheo nhịp di chuyển của bạn.',
     'GitGam Mobile tạo thêm cách truy cập không gian GitGam từ điện thoại. Đội ngũ có thể tiếp nối các tác vụ được hỗ trợ trên thiết bị di động khi rời bàn làm việc.',
     'Doanh nghiệp, nhóm làm việc linh hoạt và nhân sự cần truy cập công việc khi di chuyển.',
     [('Công việc trong ứng dụng', 'Mở không gian GitGam qua giao diện web bên trong ứng dụng mobile.'), ('Kết nối môi trường của đội', 'Sử dụng địa chỉ làm việc đã cấu hình cho doanh nghiệp.'), ('Quyền thiết bị khi cần', 'Trang được phép có thể yêu cầu camera, microphone hoặc vị trí khi có tác vụ phù hợp.'), ('Điểm truy cập linh hoạt', 'Tiếp tục sử dụng các chức năng có giao diện phù hợp với điện thoại.')],
     [('Nhận bản cài', 'Dùng bản ứng dụng được chuẩn bị cho thiết bị của doanh nghiệp.'), ('Mở đúng môi trường', 'Kiểm tra địa chỉ làm việc và đăng nhập theo quyền.'), ('Cho phép khi cần', 'Chỉ cấp quyền thiết bị cho tác vụ muốn sử dụng.')],
     [('Đội làm việc linh hoạt', 'Có thêm cách mở công việc ngoài máy tính.'), ('Nhân sự di chuyển', 'Truy cập tác vụ phù hợp trong thời gian làm việc.'), ('Doanh nghiệp dùng GitGam', 'Bổ sung điểm truy cập mobile cho môi trường hiện có.')],
     'Tính năng tùy thiết bị, quyền hệ điều hành và ứng dụng được mở. Việc phân phối bản cài được thống nhất riêng; không mặc định đã phát hành trên các kho ứng dụng.'],
    ['Mobile application', 'Stay connected to the team.\nAs your day moves.',
     'GitGam Mobile offers another way to open your GitGam workspace from a phone. Teams can continue supported mobile tasks when away from their desks.',
     'Businesses, flexible teams and employees who need access while moving between locations.',
     [('Work inside the app', 'Open GitGam through an embedded mobile web workspace.'), ('Your team’s environment', 'Use the work address configured for your business.'), ('Device access when needed', 'Authorized pages can request camera, microphone or foreground location for relevant tasks.'), ('A flexible entry point', 'Continue using features with a suitable phone interface.')],
     [('Get the application', 'Use the edition prepared for your business devices.'), ('Open the right environment', 'Check the work address and sign in with assigned access.'), ('Grant access when useful', 'Allow device permissions only for the tasks you choose.')],
     [('Flexible teams', 'Add a way to reach work beyond the computer.'), ('Employees on the move', 'Access suitable tasks during the working day.'), ('GitGam businesses', 'Add mobile entry to an existing environment.')],
     'Features depend on the device, operating-system permissions and embedded application. Distribution is agreed separately; app-store availability is not assumed.'])

add('Storage', 'GitGam Storage', 'storage', 'teal',
    ['README.md', 'AGENTS.md', 'docs/content-protection.md', 'desktop/README.md'],
    ['Lưu trữ & chia sẻ nội dung', 'Nội dung ở nơi bạn chọn.\nChia sẻ theo cách của đội.',
     'GitGam Storage hướng đến doanh nghiệp và đội nhóm muốn chia sẻ video, tệp từ máy lưu trữ của mình. Người được mời mở nội dung trên trình duyệt, còn đội ngũ chủ động quản lý nguồn dữ liệu.',
     'Doanh nghiệp, nhóm đào tạo, đội nội dung và các nhóm có kho video nội bộ.',
     [('Kho tại nơi bạn chọn', 'Chủ kho chọn thư mục trên máy lưu trữ để cung cấp nội dung.'), ('Xem trên trình duyệt', 'Người nhận mở liên kết được chia sẻ để xem video khi kết nối phù hợp.'), ('Truyền nội dung trực tiếp', 'Video và tệp đi giữa trình duyệt và máy lưu trữ qua kết nối trực tiếp.'), ('Nhận file có kiểm soát', 'Chủ kho chủ động bật nhận file vào thư mục riêng, có theo dõi tiến trình.')],
     [('Chuẩn bị kho', 'Mở ứng dụng trên máy lưu trữ và chọn nội dung muốn chia sẻ.'), ('Chia sẻ đúng người', 'Gửi liên kết dành cho người xem và giữ máy lưu trữ đang chạy.'), ('Kiểm tra trải nghiệm', 'Thử xem, tua video và truyền tệp trong điều kiện mạng thực tế.')],
     [('Đội đào tạo', 'Thử nghiệm chia sẻ video từ kho do đội quản lý.'), ('Nhóm nội dung', 'Tạo điểm xem nội dung được lựa chọn.'), ('Doanh nghiệp có kho riêng', 'Đánh giá mô hình lưu tại chỗ và xem từ trình duyệt.')],
     'Sản phẩm cần thử nghiệm theo mạng thực tế; nếu không mở được kết nối trực tiếp thì không tự chuyển qua máy chủ trung gian. DRM thương mại và kết nối tài khoản còn đang hoàn thiện; phạm vi Cloud/On-premises cần đánh giá riêng.'],
    ['Storage & content sharing', 'Content where you choose.\nSharing on your team’s terms.',
     'GitGam Storage is designed for businesses and teams sharing videos and files from their own storage computer. Invited viewers open content in a browser while the team manages the source.',
     'Businesses, training teams, content groups and teams with internal video libraries.',
     [('Your chosen storage', 'The owner selects folders on the storage computer for sharing.'), ('Browser viewing', 'Recipients open a shared viewer link when connectivity allows.'), ('Direct content transfer', 'Videos and files travel directly between the browser and storage computer.'), ('Controlled file intake', 'The owner enables uploads to a separate folder and follows transfer progress.')],
     [('Prepare the library', 'Open the storage application and choose content to share.'), ('Share with recipients', 'Send the viewer link and keep the storage computer running.'), ('Check the experience', 'Try playback, seeking and file transfer on the actual networks.')],
     [('Training teams', 'Pilot video sharing from a team-managed library.'), ('Content groups', 'Provide a viewing point for selected material.'), ('Businesses with local storage', 'Evaluate local ownership with browser access.')],
     'Pilot on actual networks: a failed direct connection does not switch to an intermediary server. Commercial DRM and account integration remain in progress; Cloud and On-premises scope needs individual assessment.'])

add('FileAttach-Server', 'GitGam FileAttach', 'paperclip', 'blue',
    ['src/route/feature.js', 'src/route/project.js', 'src/route/avatar.js', 'src/route/markdown.js'],
    ['Tệp đính kèm cho công việc', 'Đặt tài liệu cạnh công việc.\nGiữ trọn bối cảnh.',
     'GitGam FileAttach là dịch vụ hỗ trợ tệp đính kèm cho các ứng dụng GitGam. Đội ngũ có thể đặt hình ảnh, chứng từ và nội dung liên quan cạnh nghiệp vụ thay vì tách rời từng nơi.',
     'Doanh nghiệp và đội nhóm dùng tài liệu, hình ảnh trong công việc GitGam.',
     [('Tệp theo nghiệp vụ', 'Gắn nội dung liên quan vào các màn hình đã được tích hợp.'), ('Dự án & công việc', 'Hỗ trợ lưu và truy cập tệp gắn với phạm vi dự án hoặc chức năng.'), ('Ảnh & nội dung', 'Phục vụ ảnh đại diện và tài nguyên trong nội dung được hỗ trợ.'), ('Quyền theo ngữ cảnh', 'Kiểm tra quyền truy cập theo ứng dụng và loại hồ sơ liên quan.')],
     [('Kết nối dịch vụ', 'Đội triển khai cấu hình FileAttach cho ứng dụng cần dùng.'), ('Thêm đúng vị trí', 'Người dùng tải tệp tại hồ sơ hoặc công việc được hỗ trợ.'), ('Xem lại khi cần', 'Mở tài liệu trong ngữ cảnh và quyền truy cập tương ứng.')],
     [('Đội dự án', 'Đặt tài liệu tham khảo gần công việc.'), ('Phòng kế toán', 'Gắn chứng từ vào luồng nghiệp vụ đã kết nối.'), ('Doanh nghiệp', 'Có dịch vụ đính kèm dùng chung trong bộ giải pháp.')],
     'Đây là dịch vụ nền được dùng qua các ứng dụng đã tích hợp. Loại tệp, dung lượng và phạm vi quyền cần thống nhất theo từng ứng dụng.'],
    ['Attachments for business work', 'Documents beside the work.\nContext kept together.',
     'GitGam FileAttach supports attachments across integrated GitGam applications. Teams can keep images, supporting documents and related material close to the business work they describe.',
     'Businesses and teams using documents and images in GitGam workflows.',
     [('Files with context', 'Attach related content in screens that support the integration.'), ('Projects & tasks', 'Store and retrieve files associated with projects or application features.'), ('Images & content', 'Serve profile images and resources used by supported content.'), ('Contextual access', 'Check file access against the application and related record type.')],
     [('Connect the service', 'The implementation team configures FileAttach for the relevant application.'), ('Attach in the right place', 'Users upload files from a supported record or task.'), ('Return when needed', 'Open documents within the relevant context and permissions.')],
     [('Project teams', 'Keep reference material close to the work.'), ('Accounting teams', 'Attach evidence to connected accounting workflows.'), ('Businesses', 'Use a shared attachment service within the solution.')],
     'This supporting service is used through integrated applications. File types, capacity and access scope are agreed per application.'])

add('FileDocument-Server', 'GitGam FileDocument', 'folder', 'teal',
    ['src/route/document.js', 'src/route/drive.js', 'src/route/roledocument.js', 'src/route/favoritedocument.js'],
    ['Tài liệu & không gian lưu trữ', 'Tài liệu có chỗ tìm.\nĐội ngũ có chỗ cùng làm.',
     'GitGam FileDocument hỗ trợ không gian tệp và thư mục cho doanh nghiệp dùng GitGam. Các nhóm có thể tổ chức tài liệu theo dự án hoặc kho dùng chung, với quyền truy cập theo phạm vi làm việc.',
     'Đội dự án, phòng ban và doanh nghiệp cần tổ chức tài liệu làm việc.',
     [('Thư mục có tổ chức', 'Duyệt và quản lý tệp trong không gian tài liệu được kết nối.'), ('Kho theo dự án', 'Theo dõi tài liệu trong phạm vi dự án liên quan.'), ('Tìm lại thuận tiện', 'Tìm kiếm và đánh dấu tài liệu yêu thích để quay lại.'), ('Truy cập theo vai trò', 'Thiết lập quyền thư mục và thao tác tải theo phạm vi được cấp.')],
     [('Chuẩn bị không gian', 'Đội triển khai kết nối kho tài liệu với ứng dụng.'), ('Sắp xếp tài liệu', 'Tạo cấu trúc thư mục và đưa tệp vào đúng phạm vi.'), ('Chia sẻ trong đội', 'Cấp quyền phù hợp, tìm và mở lại tài liệu khi cần.')],
     [('Nhóm dự án', 'Tập hợp tài liệu theo công việc chung.'), ('Phòng ban', 'Giữ cấu trúc lưu trữ thống nhất.'), ('Doanh nghiệp', 'Phân định không gian và quyền đọc, tải tài liệu.')],
     'Dịch vụ được sử dụng qua các giao diện đã tích hợp; khả năng xem trước phụ thuộc định dạng và ứng dụng. Không mặc định có đồng biên tập tài liệu trực tuyến.'],
    ['Documents & shared storage', 'A place for documents.\nA place for the team.',
     'GitGam FileDocument supports business files and folders within GitGam. Teams can organize documents by project or shared drive, with access matched to their working scope.',
     'Project teams, departments and businesses organizing working documents.',
     [('Organized folders', 'Browse and manage files within the connected document space.'), ('Project document spaces', 'Keep documents within the relevant project scope.'), ('Easier returns', 'Search and mark favorite documents for later access.'), ('Role-based access', 'Define folder permissions and download access for authorized people.')],
     [('Prepare the space', 'The implementation team connects document storage to the application.'), ('Organize documents', 'Create a folder structure and place files in the right scope.'), ('Share within the team', 'Assign access, find documents and open them when needed.')],
     [('Project teams', 'Bring documents around shared work.'), ('Departments', 'Maintain a consistent storage structure.'), ('Businesses', 'Define spaces and permissions for reading and downloading.')],
     'The service is used through integrated interfaces. Preview depends on file format and application; live document co-editing is not assumed.'])

add('Mailer', 'GitGam Mailer', 'send', 'coral',
    ['src/route/mailer.js', 'src/config/mail.js'],
    ['Email gửi từ ứng dụng', 'Thông tin đến đúng lúc.\nKết nối thêm trọn vẹn.',
     'GitGam Mailer là dịch vụ gửi email cho các ứng dụng đã kết nối. Doanh nghiệp có thể đưa thông báo giao dịch và nội dung cần gửi vào luồng công việc, với cấu hình gửi thư được chuẩn bị tập trung.',
     'Doanh nghiệp và đội vận hành cần email phát sinh từ các ứng dụng GitGam.',
     [('Gửi từ nghiệp vụ', 'Ứng dụng được kết nối gửi nội dung email theo tác vụ.'), ('Cấu hình tập trung', 'Đội triển khai chuẩn bị dịch vụ gửi và thông tin người gửi.'), ('Nguồn gửi có kiểm soát', 'Chỉ tiếp nhận yêu cầu từ các nguồn được cấu hình và xác thực.'), ('Thành phần dùng chung', 'Bổ sung khả năng gửi thư cho các luồng đã được tích hợp.')],
     [('Chuẩn bị dịch vụ thư', 'Thống nhất tên miền gửi và nhà cung cấp phù hợp.'), ('Kết nối luồng cần dùng', 'Đội triển khai tích hợp tác vụ gửi email trong ứng dụng.'), ('Kiểm tra trước khi dùng', 'Gửi thử và xác nhận nội dung, người nhận, cấu hình gửi.')],
     [('Thông báo nghiệp vụ', 'Gửi cập nhật từ các tác vụ được tích hợp.'), ('Giao dịch doanh nghiệp', 'Chuẩn bị email phục vụ quy trình đã thống nhất.'), ('Đội vận hành', 'Có một thành phần gửi thư dùng chung để quản lý.')],
     'Mailer không phải hộp thư đọc email. Khả năng gửi và giới hạn phụ thuộc cấu hình, nhà cung cấp và uy tín tên miền; không cam kết thư luôn vào hộp thư đến.'],
    ['Application email delivery', 'Timely messages.\nA more connected workflow.',
     'GitGam Mailer sends email for connected applications. Businesses can add transactional messages to agreed workflows, with sending configuration prepared in a shared service.',
     'Businesses and operating teams needing email generated by GitGam applications.',
     [('Messages from workflows', 'Connected applications send email for relevant tasks.'), ('Shared configuration', 'The implementation team prepares the sending service and sender details.'), ('Controlled sources', 'Accept sending requests from configured, authenticated sources.'), ('A reusable service', 'Add email delivery to workflows that have been integrated.')],
     [('Prepare email delivery', 'Agree on the sending domain and a suitable mail provider.'), ('Connect the workflow', 'The implementation team integrates sending into the application.'), ('Check before use', 'Test the content, recipients and sending configuration.')],
     [('Business notifications', 'Send updates from connected tasks.'), ('Transactional workflows', 'Prepare email for agreed business processes.'), ('Operations teams', 'Manage a shared component for application email.')],
     'Mailer is not an inbox. Delivery and limits depend on configuration, the mail provider and domain reputation; inbox placement is not guaranteed.'])

add('Relay', 'GitGam Relay', 'network', 'blue',
    ['README.md', 'docs', 'src/config/relay.js'],
    ['Kết nối đến hệ thống doanh nghiệp', 'Một cầu nối phù hợp.\nMở thêm khả năng cộng tác.',
     'GitGam Relay hỗ trợ truy cập các đích nội bộ đã cấu hình thông qua một điểm kết nối trung gian. Doanh nghiệp có thêm lựa chọn khi cần đội ngũ truy cập dịch vụ trên hạ tầng của mình.',
     'Đội IT, quản trị hạ tầng và doanh nghiệp cần kết nối đến dịch vụ nội bộ.',
     [('Đích kết nối rõ ràng', 'Chỉ đưa các dịch vụ được đăng ký vào phạm vi truy cập.'), ('Kết nối từ phía nội bộ', 'Máy bên trong chủ động thiết lập kết nối ra dịch vụ Relay.'), ('Truy cập dịch vụ', 'Hỗ trợ web và các tuyến kết nối được thiết lập cho mục đích quản trị.'), ('Theo dõi kết nối', 'Đội quản trị quan sát và ngắt kết nối riêng qua công cụ đã tích hợp.')],
     [('Xác định nhu cầu', 'Chọn dịch vụ, người dùng và phạm vi truy cập cần thiết.'), ('Chuẩn bị kết nối', 'Đội kỹ thuật cấu hình Relay, máy nội bộ và quyền xác thực.'), ('Kiểm tra sử dụng', 'Mở đường truy cập đã cấp và thử các tác vụ được phép.')],
     [('Hạ tầng doanh nghiệp', 'Tạo đường truy cập có phạm vi đến dịch vụ nội bộ.'), ('Hỗ trợ từ xa', 'Cho nhân sự được cấp quyền kết nối khi cần.'), ('Vận hành GitGam', 'Bổ sung lựa chọn truy cập cho môi trường đã cấu hình.')],
     'Relay cần được cấu hình và xác thực đúng. Đây là cầu nối theo đích được cấp, không phải cam kết thay thế mọi nhu cầu mạng riêng của doanh nghiệp.'],
    ['Connections to business systems', 'A practical bridge.\nMore ways to collaborate.',
     'GitGam Relay provides an intermediary connection to configured internal targets. Businesses gain another option for authorized access to services on their own infrastructure.',
     'IT teams, infrastructure administrators and businesses connecting to internal services.',
     [('Defined destinations', 'Make registered services available within an agreed access scope.'), ('Outbound connection', 'The internal computer initiates its connection to Relay.'), ('Service access', 'Support web access and configured connection routes for administration.'), ('Connection visibility', 'Administrators inspect and disconnect individual connections through integrated tools.')],
     [('Define the need', 'Choose services, users and the required access scope.'), ('Prepare the connection', 'Technical staff configure Relay, internal targets and authentication.'), ('Verify the workflow', 'Open the authorized route and test permitted tasks.')],
     [('Business infrastructure', 'Provide scoped routes to internal services.'), ('Remote assistance', 'Let authorized staff connect when needed.'), ('GitGam operations', 'Add an access option to configured environments.')],
     'Relay requires correct configuration and authentication. It provides access to defined targets rather than a promise to replace every private-network requirement.'])

add('Static', 'GitGam Static', 'layers', 'violet',
    ['README.md', 'README.txt', 'Resources/HelpCenter/v1.0/catalog.json'],
    ['Tài nguyên dùng chung', 'Nền tảng nhất quán.\nTrải nghiệm liền mạch.',
     'GitGam Static cung cấp tài nguyên dùng chung cho các ứng dụng GitGam. Từ thành phần giao diện đến tài liệu hướng dẫn, doanh nghiệp có thêm một nền tài nguyên thống nhất để vận hành bộ sản phẩm.',
     'Đội triển khai, IT doanh nghiệp và đơn vị vận hành nhiều ứng dụng GitGam.',
     [('Thư viện dùng chung', 'Phục vụ các tài nguyên giao diện được ứng dụng tham chiếu.'), ('Tài nguyên có phiên bản', 'Tổ chức nguồn theo phiên bản để các ứng dụng sử dụng đúng bộ cần thiết.'), ('Hướng dẫn & trợ giúp', 'Cung cấp tài liệu hỗ trợ và nội dung giải đáp theo sản phẩm.'), ('Thông tin chính sách', 'Phục vụ tài liệu điều khoản và chính sách theo ngôn ngữ, phiên bản.')],
     [('Chọn môi trường', 'Đội triển khai xác định nguồn tài nguyên cho hệ thống.'), ('Kết nối ứng dụng', 'Cấu hình các ứng dụng tham chiếu đúng tài nguyên.'), ('Duy trì nhất quán', 'Quản lý phiên bản và kiểm tra hiển thị khi cập nhật.')],
     [('Bộ sản phẩm doanh nghiệp', 'Dùng nguồn tài nguyên chung giữa nhiều ứng dụng.'), ('Triển khai On-premises', 'Chuẩn bị nguồn tài nguyên trong phạm vi đã thống nhất.'), ('Đội hỗ trợ', 'Có nơi phục vụ nội dung hướng dẫn theo phiên bản.')],
     'Static là thành phần nền của bộ giải pháp. Tài nguyên và ngôn ngữ cung cấp phụ thuộc phiên bản đã được chuẩn bị cho môi trường doanh nghiệp.'],
    ['Shared platform resources', 'A consistent foundation.\nA more connected experience.',
     'GitGam Static supplies shared resources to GitGam applications. From interface libraries to help content, it provides a common resource foundation for operating the product suite.',
     'Implementation teams, business IT and operators of several GitGam applications.',
     [('Shared libraries', 'Serve interface resources referenced by connected applications.'), ('Versioned resources', 'Organize resources by version so applications use the intended edition.'), ('Guidance & help', 'Provide support documents and answers organized by product.'), ('Policy information', 'Serve terms and policy documents by language and version.')],
     [('Choose the environment', 'The implementation team identifies the resource source.'), ('Connect applications', 'Configure applications to reference the required resources.'), ('Keep versions consistent', 'Manage editions and check presentation when updating.')],
     [('Business product suites', 'Use common resources across applications.'), ('On-premises installations', 'Prepare resource delivery within the agreed environment.'), ('Support teams', 'Serve guidance organized by version.')],
     'Static is a supporting platform component. Available resources and languages depend on the editions prepared for the business environment.'])

add('OnPromise', 'GitGam On-premises', 'building', 'teal',
    ['resources/systems.json', 'resources/nginx', 'resources/pms-gateway', 'resources/tools', 'load'],
    ['Giải pháp trên hạ tầng doanh nghiệp', 'Không gian của doanh nghiệp.\nCách làm việc của đội ngũ.',
     'GitGam On-premises là lựa chọn đưa các sản phẩm GitGam vào hạ tầng của khách hàng. Doanh nghiệp cùng đội triển khai chuẩn bị môi trường phù hợp để vận hành công cụ cộng tác theo nhu cầu riêng.',
     'Doanh nghiệp có hạ tầng riêng, đội IT nội bộ và tổ chức cần chủ động môi trường triển khai.',
     [('Lựa chọn sản phẩm', 'Chọn các ứng dụng phù hợp thay vì bắt đầu với toàn bộ bộ giải pháp.'), ('Hạ tầng của khách hàng', 'Chuẩn bị máy chủ, tên miền và nguồn lực trong phạm vi thống nhất.'), ('Cấu hình phối hợp', 'Tổ chức điểm truy cập và kết nối giữa các thành phần GitGam.'), ('Vận hành có kế hoạch', 'Thống nhất người phụ trách, cập nhật, sao lưu và hỗ trợ trước khi sử dụng.')],
     [('Trao đổi yêu cầu', 'Làm rõ số người dùng, sản phẩm và môi trường hiện có.'), ('Chuẩn bị & cài đặt', 'Đội triển khai cấu hình các thành phần theo phạm vi thống nhất.'), ('Nghiệm thu & bàn giao', 'Kiểm tra luồng sử dụng và hướng dẫn đội vận hành.')],
     [('Doanh nghiệp có IT', 'Đưa công cụ GitGam vào môi trường được quản lý nội bộ.'), ('Đội nhóm cần nền tảng riêng', 'Tổ chức cách truy cập và vận hành theo nhu cầu.'), ('Triển khai theo giai đoạn', 'Bắt đầu từ ứng dụng ưu tiên rồi mở rộng sau.')],
     'Yêu cầu máy chủ, giấy phép, kết nối ngoài và phạm vi hỗ trợ được xác nhận theo dự án. On-premises không mặc định đồng nghĩa mọi chức năng đều dùng được khi không có Internet.'],
    ['On your business infrastructure', 'Your business environment.\nYour team’s way of working.',
     'GitGam On-premises brings selected GitGam products to customer-owned infrastructure. Your business and the implementation team prepare an environment suited to your collaboration needs.',
     'Businesses with their own infrastructure, internal IT teams and organizations choosing their deployment environment.',
     [('Choose your products', 'Start with the applications that fit your needs.'), ('Customer infrastructure', 'Prepare servers, domains and resources within the agreed scope.'), ('Connected configuration', 'Organize access points and connections between GitGam components.'), ('Planned operations', 'Agree on ownership, updates, backups and support before use.')],
     [('Discuss requirements', 'Define users, products and the existing environment.'), ('Prepare & install', 'The implementation team configures the agreed components.'), ('Validate & hand over', 'Check user workflows and guide the operating team.')],
     [('Businesses with IT teams', 'Bring GitGam tools into an internally managed environment.'), ('Teams choosing their platform', 'Organize access and operations around their needs.'), ('Phased adoption', 'Start with priority applications and expand later.')],
     'Server requirements, licensing, external connections and support scope are confirmed per project. On-premises does not automatically make every feature available without Internet access.'])

PALETTES = {
    'teal': ('#17675b', '#e9f5ee', '#b7d9c8'),
    'blue': ('#275a83', '#edf3fa', '#c0d7e9'),
    'violet': ('#655286', '#f3eff8', '#d7c8e8'),
    'coral': ('#97533e', '#fcf0e8', '#edcaba'),
}
CORE_ICONS = ROOT / 'PMS-Account/web/core/assets/icons/systems'
BRAND_ICONS = {
    'Account': 'account.svg', 'Accounting': 'accounting.svg',
    'Building': 'building.svg', 'Workspace': 'workspace.svg',
    'DevOps': 'devops.svg', 'HRM': 'hrm.svg', 'OfficeAdmin': 'adminpaper.svg',
    'HelpDesk': 'helpdesk.svg', 'Marketing': 'marketing.svg',
    'Producing': 'producing.svg', 'Store': 'store.svg',
    'Mailing': 'favicons/mailing-favicon.svg',
    'Messenger': 'favicons/messenger-favicon.svg', 'Home': 'favicons/home-favicon.svg',
}
# Original line drawings for the editorial illustrations, not new product logos.
DRAWINGS = {
    'key': '<circle cx="9" cy="9" r="5"/><path d="m13 13 8 8m-4-4 3-3m-6 0 3-3"/>',
    'chart': '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M7 17v-4m5 4V7m5 10v-7"/>',
    'building': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 7h1m4 0h1M9 11h1m4 0h1M9 15h1m4 0h1M10 21v-3h4v3"/>',
    'people': '<circle cx="9" cy="7" r="3"/><path d="M3 21v-4a6 6 0 0 1 12 0v4M16 4a3 3 0 0 1 0 6m3 11v-4a6 6 0 0 0-2-4"/>',
    'board': '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M3 9h18M9 9v12m6-12v12M5 6h1m3 0h1m3 0h1"/>',
    'code': '<path d="m8 6-6 6 6 6m8-12 6 6-6 6M14 3l-4 18"/>',
    'document': '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9Zm0 0v6h6M8 13h8m-8 4h5"/>',
    'support': '<path d="M4 13V9a8 8 0 0 1 16 0v8a4 4 0 0 1-4 4h-4"/><rect x="2" y="10" width="5" height="8" rx="2"/><rect x="17" y="10" width="5" height="8" rx="2"/>',
    'megaphone': '<path d="M3 10h5l12-6v16L8 14H3Zm5 4 2 7h4l-2-5M8 10v4"/>',
    'factory': '<path d="M3 21V10l6 3V8l6 4V3h5v18ZM7 17h1m3 0h1m4 0h1"/>',
    'shop': '<path d="M4 10v11h16V10M3 10l2-7h14l2 7M3 10a3 3 0 0 0 6 0 3 3 0 0 0 6 0 3 3 0 0 0 6 0M9 21v-6h6v6"/>',
    'spark': '<path d="m12 2 3 7 7 3-7 3-3 7-3-7-7-3 7-3ZM20 2v4m-2-2h4"/>',
    'mail': '<rect x="2" y="5" width="20" height="15" rx="3"/><path d="m3 7 9 7 9-7"/>',
    'chat': '<path d="M5 3h14a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3h-8l-6 3v-3a3 3 0 0 1-3-3V6a3 3 0 0 1 3-3Z"/><path d="M7 8h10M7 13h6"/>',
    'route': '<circle cx="5" cy="5" r="3"/><circle cx="19" cy="19" r="3"/><path d="M5 8v5a6 6 0 0 0 6 6h5M10 5h9v8m-4-4 4 4 4-4"/>',
    'server': '<rect x="3" y="2" width="18" height="8" rx="2"/><rect x="3" y="14" width="18" height="8" rx="2"/><path d="M7 6h.1M7 18h.1M12 6h5m-5 12h5"/>',
    'home': '<path d="m2 11 10-9 10 9M5 9v12h14V9M9 21v-7h6v7"/>',
    'desktop': '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 22h8m-4-5v5M6 7h5"/>',
    'phone': '<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 5h4m-3 14h2"/>',
    'storage': '<path d="M3 6c0-5 18-5 18 0v12c0 5-18 5-18 0ZM3 6c0 5 18 5 18 0M3 12c0 5 18 5 18 0"/>',
    'paperclip': '<path d="m9 17 9-9a3 3 0 0 0-4-4L4 14a5 5 0 0 0 7 7L21 11M7 15l9-9"/>',
    'folder': '<path d="M2 7V5a2 2 0 0 1 2-2h5l3 4h8a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2Zm0 3h20"/>',
    'send': '<path d="M22 2 9 15m13-13-8 20-5-7-7-5Z"/>',
    'network': '<rect x="8" y="2" width="8" height="6" rx="2"/><rect x="2" y="17" width="8" height="5" rx="2"/><rect x="14" y="17" width="8" height="5" rx="2"/><path d="M12 8v5H6v4m6-4h6v4"/>',
    'layers': '<path d="m12 2 10 6-10 6L2 8ZM2 13l10 6 10-6M2 18l10 6 10-6"/>',
    'cloud': '<path d="M7 19a5 5 0 0 1-1-10 7 7 0 0 1 13-1 5.5 5.5 0 0 1-1 11Z"/>',
    'check': '<path d="m5 12 4 4L20 5"/>',
    'arrow': '<path d="M3 12h18m-6-6 6 6-6 6"/>',
}

CSS = '''/* Standalone brochure: local assets, no application runtime. */
:root {
    --ink: #243c37;
    --muted: #536660;
    --paper: #fbfcf9;
    --line: #dce4de;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: 28px; }
body {
    margin: 0;
    color: var(--ink);
    background: var(--paper);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
    font-size: 16px;
    line-height: 1.65;
    -webkit-font-smoothing: antialiased;
}
a { color: inherit; }
a:focus-visible {
    outline: 3px solid var(--accent);
    outline-offset: 5px;
    border-radius: 4px;
}
p, h1, h2, h3, figure { margin: 0; }
img { display: block; max-width: 100%; }
svg { width: 24px; height: 24px; flex-shrink: 0; }
.container { max-width: 1184px; padding: 0 40px; margin: 0 auto; }
.skip-link { position: absolute; top: -100px; left: 16px; padding: 12px; background: white; }
.skip-link:focus { top: 12px; z-index: 10; }
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
    min-height: 104px;
    border-bottom: 1px solid var(--line);
}
.brand { display: flex; gap: 12px; align-items: center; text-decoration: none; }
.brand img { width: 38px; height: 38px; color: var(--accent); }
.brand strong { display: block; font-size: 19px; line-height: 1.3; }
.brand small { display: block; font-size: 11px; color: var(--muted); }
.header-right { display: flex; gap: 28px; align-items: center; }
.header-note { color: var(--muted); font-size: 12px; }
.languages { display: flex; gap: 4px; padding: 4px; border: 1px solid var(--line); border-radius: 30px; }
.languages a { text-decoration: none; padding: 7px 12px; font-size: 12px; border-radius: 30px; min-height: 36px; }
.languages a[aria-current="page"] { background: var(--accent); color: white; }
.hero { display: grid; grid-template-columns: 1.12fr 1fr; align-items: center; gap: 32px; padding: 68px 0 48px; }
.eyebrow { color: var(--accent); font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; }
h1, h2 { font-family: Georgia, "Times New Roman", serif; font-weight: 400; }
h1 { font-size: clamp(38px, 4.1vw, 55px); line-height: 1.15; letter-spacing: -1.5px; margin: 19px 0 24px; }
.intro { max-width: 580px; font-size: 17px; color: var(--muted); }
.actions { display: flex; align-items: center; flex-wrap: wrap; gap: 18px; margin-top: 28px; }
.button { display: inline-flex; gap: 12px; align-items: center; padding: 12px 20px; border-radius: 9px; text-decoration: none; font-weight: 600; font-size: 14px; }
.button svg { width: 18px; height: 18px; }
.button-primary { color: white; background: var(--accent); }
.button-light { color: var(--accent); background: white; }
.text-link { font-size: 14px; text-underline-offset: 5px; }
.hero-art { background: var(--tint); border-radius: 44% 44% 28px 28px; padding: 12px 0 16px; }
.hero-art img { width: 100%; height: auto; }
.hero-art figcaption { color: var(--muted); text-align: center; font-size: 11px; padding: 0 24px; }
.audience { display: flex; gap: 15px; align-items: flex-start; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 22px 0; font-size: 14px; }
.audience svg { color: var(--accent); }
.audience strong { display: block; color: var(--accent); font-size: 12px; margin-bottom: 2px; }
.section { padding-top: 64px; }
.section-title { display: flex; gap: 24px; justify-content: space-between; align-items: flex-end; margin-bottom: 25px; }
.section-title h2 { font-size: 34px; line-height: 1.2; margin-top: 9px; letter-spacing: -.5px; }
.section-number { color: var(--accent); font-size: 12px; font-weight: 600; }
.features { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
.feature { display: flex; align-items: flex-start; gap: 18px; padding: 27px; background: white; border: 1px solid var(--line); border-radius: 14px; }
.icon-tile { display: flex; padding: 12px; border-radius: 12px; background: var(--tint); color: var(--accent); }
h3 { font-size: 17px; line-height: 1.4; font-weight: 650; margin-bottom: 8px; }
.feature p, .step p, .application p, .deployment p { font-size: 14px; color: var(--muted); }
.steps { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; }
.step { border-top: 2px solid var(--soft); padding-top: 20px; }
.step-number { display: inline-flex; justify-content: center; align-items: center; width: 35px; height: 35px; background: var(--tint); color: var(--accent); font-size: 13px; font-weight: 700; border-radius: 50%; margin-bottom: 18px; }
.applications { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.application { padding: 23px; background: var(--tint); border-radius: 14px; }
.application svg { color: var(--accent); width: 22px; height: 22px; margin-bottom: 12px; }
.scope { margin-top: 22px; display: flex; align-items: flex-start; gap: 12px; font-size: 12px; color: var(--muted); line-height: 1.7; }
.scope svg { width: 18px; height: 18px; color: var(--accent); margin-top: 2px; }
.scope strong { color: var(--ink); }
.deployments { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }
.deployment { border: 1px solid var(--line); border-radius: 14px; padding: 26px; background: white; }
.deployment-header { display: flex; align-items: center; gap: 12px; color: var(--accent); margin-bottom: 14px; }
.deployment h3 { margin: 0; font-size: 19px; }
.deployment small { color: var(--accent); font-weight: 600; font-size: 12px; display: block; margin-top: 14px; }
.deploy-note { color: var(--muted); font-size: 12px; margin-top: 14px; }
.invitation { background: var(--accent); color: white; padding: 37px 40px; margin: 48px 0 38px; border-radius: 18px; display: flex; align-items: center; justify-content: space-between; gap: 32px; }
.invitation h2 { font-size: 30px; line-height: 1.25; margin-bottom: 12px; }
.invitation p { font-size: 14px; max-width: 650px; color: #fff; }
.invitation .button { flex-shrink: 0; }
.footer { display: flex; flex-wrap: wrap; gap: 14px; align-items: center; justify-content: space-between; border-top: 1px solid var(--line); padding: 22px 0 34px; font-size: 11px; color: var(--muted); }
.footer a { text-underline-offset: 3px; }
@media (max-width: 900px) {
    .container { padding: 0 28px; }
    .header-note { display: none; }
    .hero { gap: 20px; padding-top: 46px; }
    h1 { font-size: 41px; }
    .feature { padding: 20px; gap: 12px; }
    .icon-tile { padding: 8px; }
    .invitation { align-items: flex-start; flex-direction: column; gap: 22px; }
}
@media (max-width: 620px) {
    .container { padding: 0 22px; }
    .topbar { min-height: 88px; gap: 12px; }
    .brand { gap: 8px; }
    .brand img { width: 30px; height: 30px; }
    .brand strong { font-size: 15px; }
    .brand small { font-size: 10px; }
    .languages a { padding: 7px 10px; }
    .hero { grid-template-columns: minmax(0, 1fr); padding: 38px 0 30px; gap: 32px; }
    h1 { font-size: 40px; letter-spacing: -1px; }
    .intro { font-size: 16px; }
    .hero-art { max-width: 440px; width: 100%; justify-self: center; }
    .features, .steps, .applications, .deployments { grid-template-columns: minmax(0, 1fr); }
    .steps { gap: 22px; }
    .step { display: grid; grid-template-columns: 35px minmax(0, 1fr); column-gap: 16px; }
    .step-number { grid-row: span 2; margin: 0; }
    .section { padding-top: 42px; }
    .section-title h2 { font-size: 30px; }
    .feature { padding: 22px; }
    .application { padding: 22px; }
    .invitation { padding: 28px; margin-top: 32px; }
    .invitation h2 { font-size: 29px; }
    .eyebrow { font-size: 11px; }
}
@media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
}
'''

WORDS = {
    'vi': {
        'lang': 'vi', 'other': 'en', 'other_file': 'en.html',
        'skip': 'Đến nội dung', 'brand_note': 'Dành cho doanh nghiệp & đội nhóm',
        'edition': 'GIỚI THIỆU SẢN PHẨM', 'explore': 'Khám phá chức năng',
        'start_link': 'Cách bắt đầu', 'illustration': 'Minh họa ý tưởng · Con người, thông tin và công việc',
        'alt': 'Minh họa kết nối đội ngũ và thông tin cho', 'audience': 'PHÙ HỢP VỚI',
        'feature_label': 'CÙNG LÀM VIỆC TỐT HƠN', 'feature_title': 'Những điều bạn có thể làm',
        'start_label': 'BẮT ĐẦU TỪ ĐIỀU THIẾT THỰC', 'start_title': 'Ba bước để bắt đầu',
        'use_label': 'TỪ CÔNG CỤ ĐẾN CÔNG VIỆC', 'use_title': 'Ứng dụng trong doanh nghiệp',
        'scope': 'Cùng chuẩn bị để dùng hiệu quả.',
        'deploy_label': 'LỰA CHỌN THEO DOANH NGHIỆP', 'deploy_title': 'Cloud hay hạ tầng riêng?',
        'cloud': 'Dùng GitGam trên nền tảng cloud do GitGam cung cấp. Trao đổi nhu cầu để chọn sản phẩm và quy mô phù hợp cho đội ngũ.',
        'cloud_short': 'Một lựa chọn cho doanh nghiệp muốn dùng trên cloud.',
        'prem': 'Cài đặt trên hạ tầng của doanh nghiệp. Cùng chuẩn bị môi trường, phạm vi cài đặt và cách vận hành phù hợp với đội IT của bạn.',
        'prem_short': 'Một lựa chọn cho doanh nghiệp có hạ tầng riêng.',
        'deploy_note': 'Sản phẩm, tính năng, dung lượng, giấy phép và phạm vi hỗ trợ được thống nhất theo phương án triển khai; các dịch vụ nền được cung cấp trong bộ giải pháp phù hợp.',
        'invite': 'Bắt đầu từ nhu cầu của đội ngũ.',
        'invite_body': 'Hãy cùng GitGam chọn sản phẩm, quy mô sử dụng và cách triển khai phù hợp để doanh nghiệp bắt đầu theo nhịp của mình.',
        'visit': 'Khám phá GitGam', 'footer': 'Giới thiệu sản phẩm · Bản HTML để duyệt nội dung',
    },
    'en': {
        'lang': 'en', 'other': 'vi', 'other_file': 'index.html',
        'skip': 'Skip to content', 'brand_note': 'For businesses & teams',
        'edition': 'PRODUCT INTRODUCTION', 'explore': 'Explore the features',
        'start_link': 'How to get started', 'illustration': 'Concept illustration · People, information and work',
        'alt': 'An illustration of connected teams and information for', 'audience': 'MADE FOR',
        'feature_label': 'MAKE ROOM FOR BETTER WORK', 'feature_title': 'What you can do',
        'start_label': 'START WITH SOMETHING PRACTICAL', 'start_title': 'Three steps to get started',
        'use_label': 'FROM TOOLS TO EVERYDAY WORK', 'use_title': 'Where it fits in your business',
        'scope': 'Prepare for a useful experience.',
        'deploy_label': 'CHOOSE WHAT FITS YOUR BUSINESS', 'deploy_title': 'Cloud or your infrastructure?',
        'cloud': 'Use GitGam on the cloud platform provided by GitGam. Discuss your needs to choose suitable products and capacity for your team.',
        'cloud_short': 'An option for businesses choosing cloud delivery.',
        'prem': 'Install on your business infrastructure. Agree on the environment, installation scope and operating approach with your IT team.',
        'prem_short': 'An option for businesses with their own infrastructure.',
        'deploy_note': 'Products, features, capacity, licensing and support are agreed for the deployment plan. Supporting services are supplied within the appropriate solution.',
        'invite': 'Start with what your team needs.',
        'invite_body': 'Work with GitGam to choose suitable products, usage scale and deployment, and begin at a pace that fits your business.',
        'visit': 'Discover GitGam', 'footer': 'Product introduction · HTML edition for review',
    },
}


def esc(value):
    return html.escape(str(value), quote=True)


def icon(name, class_name=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
            f'class="{class_name}">{DRAWINGS[name]}</svg>')


def illustration(product):
    accent, tint, soft = PALETTES[product['color']]

    def glyph(name, x, y, scale):
        return (f'<g transform="translate({x} {y}) scale({scale})" fill="none" '
                f'stroke="{accent}" stroke-width="1.5" stroke-linecap="round" '
                f'stroke-linejoin="round">{DRAWINGS[name]}</g>')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 420" fill="none">
    <!-- Original editorial illustration for {esc(product['name'])}. -->
    <ellipse cx="263" cy="366" rx="203" ry="15" fill="{soft}" opacity=".35"/>
    <circle cx="278" cy="185" r="145" fill="{soft}" opacity=".33"/>
    <circle cx="424" cy="91" r="26" fill="#f4d6a5"/>
    <path d="M88 128c38-39 80-48 117-35M354 308c40-6 58-27 70-50" stroke="{accent}" stroke-opacity=".25" stroke-width="2" stroke-dasharray="5 8"/>
    <path d="m127 137 104 63m137-82-65 78m71 102-75-54" stroke="{accent}" stroke-opacity=".4" stroke-width="2"/>
    <rect x="154" y="134" width="231" height="179" rx="21" fill="{soft}" opacity=".6"/>
    <rect x="145" y="124" width="231" height="179" rx="21" fill="white" stroke="{soft}"/>
    <rect x="145" y="124" width="231" height="42" rx="21" fill="{tint}"/>
    <path d="M146 149v17h229v-17" fill="{tint}"/>
    <circle cx="166" cy="145" r="4" fill="{soft}"/>
    <circle cx="180" cy="145" r="4" fill="{soft}"/>
    <circle cx="194" cy="145" r="4" fill="{soft}"/>
    <rect x="221" y="183" width="78" height="78" rx="23" fill="{tint}"/>
    {glyph(product['icon'], 236, 198, 2)}
    <path d="M216 280h88" stroke="{soft}" stroke-width="6" stroke-linecap="round"/>
    <rect x="48" y="77" width="107" height="110" rx="18" fill="white" stroke="{soft}"/>
    <circle cx="102" cy="118" r="25" fill="{tint}"/>
    {glyph('people', 89, 103, 1.1)}
    <path d="M78 159h49" stroke="{soft}" stroke-width="5" stroke-linecap="round"/>
    <rect x="359" y="46" width="101" height="101" rx="18" fill="white" stroke="{soft}"/>
    {glyph('document', 390, 63, 1.6)}
    <path d="M386 124h45" stroke="{soft}" stroke-width="5" stroke-linecap="round"/>
    <rect x="346" y="266" width="123" height="79" rx="17" fill="white" stroke="{soft}"/>
    <circle cx="376" cy="305" r="17" fill="{tint}"/>
    {glyph('check', 364, 293, 1)}
    <path d="M407 299h39m-39 13h26" stroke="{soft}" stroke-width="5" stroke-linecap="round"/>
    <path d="M78 348v-53m0 31c-25-1-31-15-29-27 20 0 29 10 29 27Zm0-14c20-1 27-15 25-29-20 2-25 13-25 29Z" fill="{soft}" stroke="{accent}" stroke-opacity=".6" stroke-width="1.5"/>
    <path d="M58 337h40l-7 28H65Z" fill="#e5c5a7"/>
    <circle cx="176" cy="65" r="5" fill="{accent}" opacity=".3"/>
    <path d="M312 66v12m-6-6h12M126 324v10m-5-5h10" stroke="{accent}" stroke-opacity=".4" stroke-width="2"/>
</svg>
'''


def heading(label, title, number):
    return f'''<div class="section-title">
                <div><p class="eyebrow">{esc(label)}</p><h2>{esc(title)}</h2></div>
                <span class="section-number" aria-hidden="true">{number:02d}</span>
            </div>'''


def render(product, locale):
    words = WORDS[locale]
    category, headline, intro, audience, features, steps, uses, note = product[locale]
    accent, tint, soft = PALETTES[product['color']]
    feature_icons = [product['icon'], 'people', 'board', 'check']
    feature_html = '\n'.join(f'''                <article class="feature">
                    <span class="icon-tile">{icon(feature_icons[i])}</span>
                    <div><h3>{esc(title)}</h3><p>{esc(body)}</p></div>
                </article>''' for i, (title, body) in enumerate(features))
    step_html = '\n'.join(f'''                <article class="step">
                    <span class="step-number" aria-hidden="true">{i + 1:02d}</span>
                    <h3>{esc(title)}</h3><p>{esc(body)}</p>
                </article>''' for i, (title, body) in enumerate(steps))
    use_html = '\n'.join(f'''                <article class="application">
                    {icon(['people', 'building', 'spark'][i])}
                    <h3>{esc(title)}</h3><p>{esc(body)}</p>
                </article>''' for i, (title, body) in enumerate(uses))
    vi_current = ' aria-current="page"' if locale == 'vi' else ''
    en_current = ' aria-current="page"' if locale == 'en' else ''
    title_lines = '<br>'.join(esc(line) for line in headline.split('\n'))
    language_label = 'Ngôn ngữ' if locale == 'vi' else 'Language'

    return f'''<!doctype html>
<html lang="{locale}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{esc(intro)}">
    <meta name="color-scheme" content="light">
    <title>{esc(product['name'])} — {esc(category)}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="assets/product.svg" type="image/svg+xml">
    <link rel="alternate" hreflang="{words['other']}" href="{words['other_file']}">
</head>
<body style="--accent: {accent}; --tint: {tint}; --soft: {soft};">
    <a class="skip-link" href="#main">{esc(words['skip'])}</a>
    <div class="container">
        <header class="topbar">
            <a class="brand" href="#main">
                <img src="assets/product.svg" alt="" width="38" height="38">
                <span><strong>{esc(product['name'])}</strong><small>{esc(category)}</small></span>
            </a>
            <div class="header-right">
                <span class="header-note">{esc(words['brand_note'])}</span>
                <nav class="languages" aria-label="{language_label}">
                    <a href="index.html" lang="vi" hreflang="vi"{vi_current}>VI</a>
                    <a href="en.html" lang="en" hreflang="en"{en_current}>EN</a>
                </nav>
            </div>
        </header>
        <main id="main">
            <section class="hero" aria-labelledby="headline">
                <div>
                    <p class="eyebrow">{esc(words['edition'])}</p>
                    <h1 id="headline">{title_lines}</h1>
                    <p class="intro">{esc(intro)}</p>
                    <div class="actions">
                        <a class="button button-primary" href="#features">{esc(words['explore'])}{icon('arrow')}</a>
                        <a class="text-link" href="#start">{esc(words['start_link'])}</a>
                    </div>
                </div>
                <figure class="hero-art">
                    <img src="assets/illustration.svg" alt="{esc(words['alt'])} {esc(product['name'])}" width="520" height="420">
                    <figcaption>{esc(words['illustration'])}</figcaption>
                </figure>
            </section>
            <aside class="audience">
                {icon('people')}
                <div><strong>{esc(words['audience'])}</strong><p>{esc(audience)}</p></div>
            </aside>
            <section class="section" id="features" aria-labelledby="features-title">
                {heading(words['feature_label'], words['feature_title'], 1).replace('<h2>', '<h2 id="features-title">')}
                <div class="features">
{feature_html}
                </div>
            </section>
            <section class="section" id="start" aria-labelledby="start-title">
                {heading(words['start_label'], words['start_title'], 2).replace('<h2>', '<h2 id="start-title">')}
                <div class="steps">
{step_html}
                </div>
            </section>
            <section class="section" aria-labelledby="applications-title">
                {heading(words['use_label'], words['use_title'], 3).replace('<h2>', '<h2 id="applications-title">')}
                <div class="applications">
{use_html}
                </div>
                <aside class="scope">{icon('document')}<p><strong>{esc(words['scope'])}</strong> {esc(note)}</p></aside>
            </section>
            <section class="section" aria-labelledby="deploy-title">
                {heading(words['deploy_label'], words['deploy_title'], 4).replace('<h2>', '<h2 id="deploy-title">')}
                <div class="deployments">
                    <article class="deployment">
                        <div class="deployment-header">{icon('cloud')}<h3>GitGam Cloud</h3></div>
                        <p>{esc(words['cloud'])}</p><small>{esc(words['cloud_short'])}</small>
                    </article>
                    <article class="deployment">
                        <div class="deployment-header">{icon('server')}<h3>On-premises</h3></div>
                        <p>{esc(words['prem'])}</p><small>{esc(words['prem_short'])}</small>
                    </article>
                </div>
                <p class="deploy-note">{esc(words['deploy_note'])}</p>
            </section>
            <section class="invitation" aria-labelledby="invite-title">
                <div><h2 id="invite-title">{esc(words['invite'])}</h2><p>{esc(words['invite_body'])}</p></div>
                <a class="button button-light" href="https://gitgam.com" target="_blank" rel="noopener noreferrer">{esc(words['visit'])}{icon('arrow')}</a>
            </section>
        </main>
        <footer class="footer">
            <span>{esc(product['name'])} · {esc(words['footer'])}</span>
            <a href="{words['other_file']}" hreflang="{words['other']}" lang="{words['other']}">{'Read in English' if locale == 'vi' else 'Đọc bằng tiếng Việt'}</a>
        </footer>
    </div>
</body>
</html>
'''


def build():
    manifest = []
    for product in PRODUCTS:
        root = ROOT / ('PMS-' + product['repo'])
        destination = root / 'brochure'
        assets = destination / 'assets'
        assets.mkdir(parents=True, exist_ok=True)
        (destination / 'index.html').write_text(render(product, 'vi'))
        (destination / 'en.html').write_text(render(product, 'en'))
        (destination / 'styles.css').write_text(CSS)
        brand = CORE_ICONS / BRAND_ICONS.get(product['repo'], 'ecosystem.svg')
        brand_content = brand.read_text()
        # External SVG images cannot inherit currentColor from the HTML parent.
        (assets / 'product.svg').write_text(brand_content.replace('currentColor', PALETTES[product['color']][0]))
        (assets / 'illustration.svg').write_text(illustration(product))
        (assets / 'LICENSE.txt').write_text((CORE_ICONS / 'LICENSE').read_text())
        (destination / 'README.txt').write_text(
            product['name'] + ' — Brochure / Tài liệu giới thiệu\n'
            '================================================\n\n'
            'Mở index.html cho tiếng Việt; mở en.html cho English.\n'
            'Open index.html for Vietnamese or en.html for English.\n'
            'Giữ cả thư mục để hình và stylesheet đi cùng HTML.\n'
            'Keep the folder together so images and styles remain available.\n'
            'No server, build, external fonts or scripts are required.\n'
            'HTML review edition. PDF export waits for content/design approval.\n'
            'Audience: businesses and teams. Delivery: GitGam Cloud / On-premises.\n'
            'Supporting services are scoped as part of the business solution.\n\n'
            'Content references / Căn cứ nội dung (repository-relative):\n'
            + '\n'.join('- ' + source for source in product['sources'])
            + '\n\nProduct mark: reused from the existing Web Core icon collection;\n'
            'where no dedicated mark exists, the shared ecosystem mark is used.\n'
            'Icon notices: assets/LICENSE.txt and comments in assets/product.svg.\n'
            'Editorial illustration: original SVG, conceptual rather than an app screenshot.\n'
            'Brochure assets are independent documentation; application code is unchanged.\n')
        manifest.append(dict(repo=root.name, name=product['name'],
                             path=str(destination), sources=product['sources']))
    REPORT.mkdir(parents=True, exist_ok=True)
    (REPORT / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=4) + '\n')
    cards = '\n'.join(f'<article><h2>{esc(item["name"])}</h2><p><a href="{esc(item["path"])}/index.html">Tiếng Việt</a> · <a href="{esc(item["path"])}/en.html">English</a></p><p><a href="screenshots/{item["repo"]}-vi-desktop.png">Ảnh desktop</a> · <a href="screenshots/{item["repo"]}-vi-mobile.png">Ảnh mobile</a></p></article>' for item in manifest)
    (REPORT / 'index.html').write_text(f'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>GitGam — Duyệt 27 brochure sản phẩm</title>
<style>body{{font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:40px;background:#fbfcf9;color:#243c37}}main{{max-width:1100px;margin:auto}}h1{{font:42px/1.2 Georgia,serif}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px}}article{{border:1px solid #dce4de;border-radius:14px;padding:22px;background:white}}h2{{font-size:20px}}a{{color:#17675b;text-underline-offset:4px}}.note{{max-width:800px;margin-bottom:32px}}</style></head><body><main><h1>GitGam · Bộ brochure sản phẩm</h1><p class="note">27 sản phẩm · Tiếng Việt & English · Dành cho doanh nghiệp và đội nhóm · GitGam Cloud & On-premises. Chọn bản HTML để duyệt toàn bộ nội dung; ảnh desktop/mobile được lưu từ browser. Chưa xuất PDF, chưa deploy.</p><div class="grid">{cards}</div></main></body></html>\n''')
    print(f'Built {len(manifest)} brochure folders, {len(manifest) * 2} HTML documents.')


if __name__ == '__main__':
    build()
